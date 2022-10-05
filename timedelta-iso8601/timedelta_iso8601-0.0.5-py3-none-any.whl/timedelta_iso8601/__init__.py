import datetime

_DURATION_UNITS = {
    "Y": "years",
    "M": "months",
    "D": "days",
}
_TIME_UNITS = {
    "H": "hours",
    "M": "minutes",
    "S": "seconds",
}
_WEEK_UNITS = {
    "W": "weeks",
}

_DECIMAL_SEPARATORS = frozenset(".,")
_FIELD_SEPARATORS = frozenset("-:")

_GREGORIAN_MAXIMA = {
    "months": 12,
    "days_of_year": 366,
    "days_of_month": 31,
    "hours": 23,
    "minutes": 59,
    "seconds": 59,
}


class timedelta(datetime.timedelta):
    def _denormalize(self):
        days, hours, minutes, seconds = self.days, 0, 0, self.seconds
        days, seconds = days + int(seconds / 86400), seconds % 86400
        hours, seconds = hours + int(seconds / 3600), seconds % 3600
        minutes, seconds = minutes + int(seconds / 60), seconds % 60
        seconds += self.microseconds / 10**6 if self.microseconds else 0
        return days, hours, minutes, seconds

    def isoformat(self, concise=False):
        """Return the duration formatted according to ISO."""
        if self and not any([self.seconds, self.microseconds, self.days % 7]):
            return f"P{int(self.days / 7)}W"

        days, hours, minutes, seconds = self._denormalize()
        if concise:
            if days and hours:
                days, hours = 0, days * 24 + hours
            if hours and minutes:
                hours, minutes = 0, hours * 60 + minutes

        duration, time = str(), str()
        if days:
            duration += f"{days}D"
        if hours:
            time += f"{hours}H"
        if minutes:
            time += f"{minutes}M"
        if seconds:
            time += f"{seconds}S"
        if time:
            duration += f"T{time}"
        if duration:
            return f"P{duration}"
        else:
            return "P0D"

    @classmethod
    def _parse_duration(cls, date_string):
        date_length = len(date_string)
        if not len("YYYYDDD") <= date_length <= len("YYYY-MM-DD"):
            raise ValueError(f"unable to parse '{date_string}' as a date")

        def dash_positions(text):
            return set([i for i, char in enumerate(text) if char == "-"])

        # YYYY-DDD
        if date_length == 8 and dash_positions(date_string) == {4}:
            yield "years", int(date_string[0:4])
            yield "days_of_year", int(date_string[5:8])

        # YYYYDDD
        if date_length == 7 and date_string.isnumeric():
            yield "years", int(date_string[0:4])
            yield "days_of_year", int(date_string[4:7])

        # YYYY-MM-DD
        if date_length == 10 and dash_positions(date_string) == {4, 7}:
            yield "years", int(date_string[0:4])
            yield "months", int(date_string[5:7])
            yield "days_of_month", int(date_string[8:10])

        # YYYYMMDD
        if date_length == 8 and date_string.isnumeric():
            yield "years", int(date_string[0:4])
            yield "months", int(date_string[4:6])
            yield "days_of_month", int(date_string[6:8])

    @classmethod
    def _parse_time(cls, time_string):
        time_length = len(time_string)
        if not len("HHMMSS") <= time_length <= len("HH:MM:SS.ssssss"):
            raise ValueError(f"unable to parse {time_string} as a time")

        def colon_positions(text):
            return set([i for i, char in enumerate(text) if char == ":"])

        # HH:MM:SS[.ssssss]
        if time_length >= 8 and colon_positions(time_string) == {2, 5}:
            if time_length == 8 or time_string[8] == ".":
                yield "hours", int(time_string[0:2])
                yield "minutes", int(time_string[3:5])
                yield "seconds", float(time_string[6:])

        # HHMMSS[.ssssss]
        if time_length >= 6 and time_string.isdigit():
            if time_length == 6 or time_string[6] == ".":
                yield "hours", int(time_string[0:2])
                yield "minutes", int(time_string[2:4])
                yield "seconds", float(time_string[4:])

    @classmethod
    def _filter_values(cls, pairs):
        for k, v in pairs:
            max = _GREGORIAN_MAXIMA.get(k, v)
            if not 0 <= v <= max:
                raise ValueError(f"{k}: {v} exceeds calendar range 0..{max}")
            k = "days" if k.startswith("days_of") else k
            if k == "days" or v:
                yield k, v

    @classmethod
    def _parse_isoformat(cls, duration_string, time_format=False):
        if not next(duration_string, None) == "P":
            raise ValueError("must start with the character 'P'")

        duration_designators = iter(["Y", "M", "D"])
        time_designators = iter(["H", "M", "S"])
        week_designators = iter(["W"])
        designators, units = duration_designators, _DURATION_UNITS

        numeral, cast, designator = str(), int, None
        for char in duration_string:
            if char.isdigit():
                numeral += char
                continue

            if char in _FIELD_SEPARATORS:
                numeral += char
                continue

            if char in _DECIMAL_SEPARATORS:
                if not numeral:
                    raise ValueError("integer part required in decimals")
                if cast == float:
                    raise ValueError("maximum one decimal point per numeral")
                numeral += "."
                cast = float
                continue

            if char == "T":
                if numeral and designator:
                    raise ValueError(f"unexpected content after {designator}")
                if numeral:
                    yield from cls._filter_values(cls._parse_duration(numeral))
                    numeral, cast = str(), int
                designators, units = time_designators, _TIME_UNITS
                continue

            if char == "W":
                designators, units = week_designators, _WEEK_UNITS
                pass

            designator = char if char in designators else None
            if not designator:
                raise ValueError(f"unexpected character '{char}'")
            if not numeral:
                raise ValueError(f"missing number before '{char}'")

            yield units[designator], cast(numeral)
            numeral, cast = str(), int

        if numeral and designator:
            raise ValueError(f"unexpected content after {designator}")
        if numeral:
            parsers = {
                duration_designators: cls._parse_duration,
                time_designators: cls._parse_time,
            }
            yield from cls._filter_values(parsers[designators](numeral))

    @classmethod
    def fromisoformat(cls, duration_string):
        """Construct a duration from a string in ISO 8601 format."""
        if not isinstance(duration_string, str):
            raise TypeError("fromisoformat: argument must be str")

        def _invalid_format(reason):
            msg = f"Invalid isoformat string '{duration_string}': {reason}"
            return ValueError(msg)

        if duration_string.endswith("T"):
            raise _invalid_format("incomplete time-string")

        try:
            measurements = dict(cls._parse_isoformat(iter(duration_string)))
        except ValueError as e:
            raise _invalid_format(e)
        if not measurements:
            raise _invalid_format("no duration measurements found")
        if "weeks" in measurements and len(measurements.keys()) > 1:
            raise _invalid_format("cannot mix weeks with other units")

        try:
            return cls(**measurements)
        except TypeError:
            msg = "Unsupported: could not create timedelta for this duration"
            raise NotImplementedError(msg)
