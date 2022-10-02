"""
- Authors: Peter Mawhorter
- Consulted:
- Date: 2022-9-4
- Purpose: Parsing for journal-format exploration records.

A journal fundamentally consists of a number of lines detailing
decisions reached, options observed, and options chosen. Other
information like enemies fought, items acquired, or general comments may
also be present.

The start of each line is a single letter that determines the entry
type, and remaining parts of that line separated by whitespace determine
the specifics of that entry. Indentation is allowed and ignored; its
suggested use is to indicate which entries apply to previous entries
(e.g., tags, annotations, effects, and requirements).

The `convertJournal` function converts a journal string into a
`core.Exploration` object, or adds to an existing exploration object if
one is specified.

To support slightly different journal formats, a `Format` dictionary is
used to define the exact notation used for various things.
"""

from typing import (
    Optional, List, Tuple, Dict, Union, Literal, Collection, get_args,
    cast
)

import re
import warnings

from . import core


#----------------------#
# Parse format details #
#----------------------#

JournalEntryType = Literal[
    'START',
    'explore',
    'return',
    'action',
    'retrace',
    'warp',
    'wait',
    'observe',
    'END',

    'requirement',
    'effect',
    'apply',

    'tag',
    'annotate',

    'zone',

    'unify',
    'obviate',

    'relative'
]
"""
One of the types of entries that can be present in a journal. Each
journal line is either an entry or a continuation of a previous entry.
The available types are:

- 'START': Names the starting decision; must appear first except in
    journal fragments.
- 'explore': Names a transition taken and the decision reached as a
    result, possible with a name for the reciprocal transition which is
    created.
- 'return': Names a transition taken and decision returned to,
    connecting a transition which previously connected to an unexplored
    area back to a known decision instead.
- 'action': Names an action taken at the current decision and may
    include effects and/or requirements.
- 'retrace': Names a transition taken, where the destination is already
    explored.
- 'wait': indicates a step of exploration where no transition is taken,
    optionally with effects that occur. Use 'action' instead for
    player-initiated effects.
- 'warp': Names a new decision to be at, but without adding a transition
    there from the previous decision.
- 'observe': Names a transition observed from the current decision, or a
    transition plus destination if the destination is known, or a
    transition plus destination plus reciprocal if reciprocal
    information is also available. Observations don't create exploration
    steps.
- 'END': Names an ending which is reached from the current decision via
    a new automatically-named transition.

- 'requirement': Specifies a requirement to apply to the
    most-recently-defined transition or its reciprocal.
- 'effect': Specifies an effect to add to the most-recently-defined
    transition or its reciprocal. The remainder of the line should be
    parsable using `ParseFormat.parseEffect`.
- 'apply': Specifies an effect to be immediately applied to the current
    state, relative to the most-recently-taken or -defined transition. If
    a 'transition' target specifier is included, the effect will also be
    recorded as an effect of the most-recently-taken transition, but
    otherwise it will just be applied without being stored in the graph.
    Use this to capture surprising effects which only became apparent
    after a transition was taken, or without the transition target to
    specify changes that occurred without being associated with a
    transition (especially one-time changes).

- 'tag': Applies one or more tags to the current decision, or to either
    the most-recently-taken transition or its reciprocal if a target
    part is specified.
- 'annotate': Like 'tag' but applies an annotation.

- 'zone': Specifies a zone name that all subsequent decisions will be
    added to, or possibly a higher-order zone that subsequent zones will
    be added to. Can also be used to stop zone-adding if used without a
    name.

- 'unify': Specifies a decision with which the current decision will be
    unified (or two decisions that will be unified with each other),
    merging their transitions. Can instead target a transition or
    reciprocal to merge (which must be at the current decision), although
    the transition to merge with must either lead to the same destination
    or lead to an unknown destination (which will then be merged with the
    transition's destination).
- 'obviate': Specifies a transition at the current decision and a
    decision that it links to and updates that information, without
    actually crossing the transition. May specify a specific reciprocal
    as well.

- 'relative': Specifies a decision to be treated as the 'current
    decision' without actually setting the position there. Until used to
    reverse this effect, all position-changing entries change this
    relative position value instead of the actual position in the graph,
    and updates are applied to the current graph without creating new
    exploration steps or applying any effects. Useful for doing things
    like noting information about far-away locations disclosed in a
    cutscene. Can target a transition at the current node, in which case
    that is counted as the 'most-recent-transition' for entry purposes
    and the same relative mode is entered.
"""

JournalTargetType = Literal[
    'transitionPart',
    'reciprocalPart',
    'zonePart',
]
"""
The different parts that an entry can target. The signifiers for these
target types will be concatenated with a journal entry signifier in some
cases. For example, by default 't' as an entry type means 'tag', and 't'
as a target type means 'transition'. So 'tt' as an entry type means 'tag
transition' and applies the relevant tag to the most-recently-created
transition instead of the most-recently-created decision. The available
target parts are:

- 'transitionPart' Use in addition to an entry type to specify that the
    entry type applies to a transition instead of a decision. Only valid
    for certain types like 'tag'.
- 'reciprocalPart' Use in addition to an entry type to specify that the
    entry type applies to a reciprocal transition instead of a decision.
    Only valid for certain types like 'tag'.

The entry types where a target specifier can be applied are:

- 'requirement': By default these are applied to transitions, but the
    'reciprocalPart' target can be used to apply to a reciprocal
    instead.
- 'effect': Same as 'requirement'.
- 'apply': Same as 'requirement'.
- 'tag': Applies the tag to the specified target instead of the
    most-recently-created decision, which is the default.
- 'annotation': Same as 'tag'.
- 'unify': By default applies to a decision, but can be applied to a
    transition or reciprocal instead.
- 'relative': Only 'transition' applies here and changes the
    most-recent-transition value when entering relative mode instead of
    just changing the current-decision value. Can be used within
    relative mode to pick out an existing transition as well.
- 'zone': This is the only place where the 'zone' target type applies.
    And it can actually be applied as many times as you want. Each
    application makes the zone specified (or end-of-zone specified)
    apply to a higher level in the hierarchy of zones, so that instead
    of adding decisions to a zone using 'z', zones are added to a zone
    defined using 'zz', and these zones-of-zones can be placed in zones
    specified using 'zzz', etc.
"""

JournalInfoType = Literal[
    'comment',
    'unknownItem',
    'tokenQuantity',
    'requirement',
    'reciprocalSeparator',
    'transitionAtDecision',
    'blockDelimeters',
]
"""
Represents a part of the journal syntax which isn't an entry type but is
used to mark something else. For example, the character denoting an
unknown item. The available values are:

- 'unknownItem': Used in place of an item name to indicate that
    although an item is known to exist, it's not yet know what that item
    is. Note that when journaling, you should make up names for items
    you pick up, even if you don't know what they do yet. This notation
    should only be used for items that you haven't picked up because
    they're inaccessible, and despite being apparent, you don't know
    what they are because they come in a container (e.g., you see a
    sealed chest, but you don't know what's in it).
- 'tokenQuantity': This is used to separate a token name from a token
    quantity when defining items picked up. Note that the parsing for
    requirements is not as flexible, and always uses '*' for this, so to
    avoid confusion it's preferable to leave this at '*'.
- 'reciprocalSeparator': Used to indicate, within a requirement or a
    tag set, a separation between requirements/tags to be applied to the
    forward direction and requirements/tags to be applied to the reverse
    direction. Not always applicable (e.g., actions have no reverse
    direction).
- 'transitionAtDecision' Used to separate a decision name from a
    transition name when identifying a specific transition.
- 'blockDelimeters' Two characters used to delimit the start and end of
    a block of entries. Used for things like edit effects.
"""

JournalEffectType = Literal[
    'gain',
    'lose',
    'toggle',
    'deactivate',
    'edit'
]
"""
Represents a type of effect. The available types are:

- 'gain': The player gains powers and/or tokens. Multiple powers/tokens
    can be listed in a single effect line. Use the 'tokenQuantity' glyph
    to distinguish between powers and tokens (e.g., 'key' is a power,
    but 'key*1' is a single key token, if '*' is the 'tokenQuantity'
    marker).
- 'lose': The inverse of 'gain'.
- 'toggle': Lists multiple powers that will be toggled on/off in turn on
    successive transitions. If there's just one power, it is gained and
    then lost in success, if there are multiple, the *n*th transition
    will cause the player to gain the *n*th power, and lose all of the
    other listed powers. TODO: Toggling for game states!
- 'deactivate': Deactivates the transition it is associated with, by
    setting the requirement to `ReqImpossible`.
- 'edit': This is the most complex effect: it is followed by a pair of
    'blockDelimeters` spread across multiple lines, and the lines in
    between can contain arbitrary commands to be executed in relative
    mode where the target starts as the decision + transition that the
    effect is being attached to. The commands in the block cannot exit
    relative mode (such a command will be ignored) and so they only edit
    the graph without adding steps. When the transition is taken, those
    edits will be applied to the graph. TODO: less clumsy way of doing
    toggling edits?
"""

JournalEffectModifier = Literal[
    'charges',
    'delay',
]
"""
A modifier that can apply to an effect. One of:

- 'charges': Specifies that the effect can only be applied a certain
    number of times before being used up. An effect with charges
    subtracts one charge each time it is applied. If it has zero
    or negative charges, it will be skipped, and the number of charges
    will not be decremented.
- 'delay': Specifies that an effect doesn't apply until the nth time it
    would normally apply. Whenever an effect with a delay would normally
    be applied, instead the delay value is reduced by 1. Only if the
    delay value is zero or negative does the effect actually apply (and
    in that case, the delay value is unchanged).
"""

JournalMarkerType = Union[
    JournalEntryType,
    JournalTargetType,
    JournalInfoType,
    JournalEffectType,
    JournalEffectModifier
]
"Any journal marker type."


Format = Dict[JournalMarkerType, str]
"""
A journal format is specified using a dictionary with keys that denote
journal marker types and values which are one-to-several-character
strings indicating the markup used for that entry/info type.
"""

DEFAULT_FORMAT: Format = {
    # Core methods
    'START': 'S',
    'explore': 'x',
    'return': 'R',
    'action': 'a',
    'retrace': 'r',
    'wait': 'w',
    'warp': 'p',
    'observe': 'o',
    'END': 'E',

    # Transition properties
    'requirement': 'q',
    'effect': 'e',
    'apply': 'A',

    # Tags & annotations
    'tag': 't',
    'annotate': 'n',

    # Zones
    'zone': 'z',

    # Revisions
    'unify': 'u',
    'obviate': 'v',

    # Relative mode
    'relative': '@',

    # Target specifiers
    'transitionPart': 't',
    'reciprocalPart': 'r',
    'zonePart': 'z',

    # Info markers
    'comment': '#',
    'unknownItem': '?',
    'tokenQuantity': '*',
    'reciprocalSeparator': '/',
    'transitionAtDecision': ':',
    'blockDelimeters': '[]',

    # Effect types
    'gain': 'gain',
    'lose': 'lose',
    'toggle': 'toggle',
    'deactivate': 'deactivate',
    'edit': 'edit',

    # Effect modifiers
    'charges': '*',
    'delay': ',',
}
"""
The default `Format` dictionary.
"""


class ParseFormat:
    """
    A ParseFormat manages the mapping from markers to entry types and
    vice versa.
    """
    def __init__(self, formatDict: Format = DEFAULT_FORMAT):
        """
        Sets up the parsing format. Requires a `Format` dictionary to
        define the specifics. Raises a `ValueError` unless the keys of
        the `Format` dictionary exactly match the `JournalMarkerType`
        values.
        """
        self.formatDict = formatDict

        # Build comment RE
        self.commentRE = re.compile(
            formatDict.get('comment', '#') + '.*$',
            flags=re.MULTILINE
        )

        # Check that formatDict doesn't have any extra keys
        markerTypes = (
            get_args(JournalEntryType)
          + get_args(JournalTargetType)
          + get_args(JournalInfoType)
          + get_args(JournalEffectType)
          + get_args(JournalEffectModifier)
        )
        for key in formatDict:
            if key not in markerTypes:
                raise ValueError(
                    f"Format dict has key '{key}' which is not a"
                    f" recognized entry or info type."
                )

        # Check completeness of formatDict
        for mtype in markerTypes:
            if mtype not in formatDict:
                raise ValueError(
                    f"Format dict is missing an entry for marker type"
                    f" '{mtype}'."
                )

        # Build reverse dictionaries from markers to entry types and
        # from markers to target types (no reverse needed for info
        # types).
        self.entryMap: Dict[str, JournalEntryType] = {}
        self.targetMap: Dict[str, JournalTargetType] = {}
        self.effectMap: Dict[str, JournalEffectType] = {}
        self.effectModMap: Dict[str, JournalEffectModifier] = {}
        entryTypes = set(get_args(JournalEntryType))
        targetTypes = set(get_args(JournalTargetType))
        effectTypes = set(get_args(JournalEffectType))
        effectModifierTypes = set(get_args(JournalEffectModifier))

        # Check for duplicates and create reverse maps
        for name, marker in formatDict.items():
            if name in entryTypes:
                # Duplicates not allowed among entry types
                if marker in self.entryMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.entryMap[marker]}'."
                    )

                # Map markers to entry types
                self.entryMap[marker] = cast(JournalEntryType, name)
            elif name in targetTypes:
                # Duplicates not allowed among entry types
                if marker in self.targetMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.targetMap[marker]}'."
                    )

                # Map markers to entry types
                self.targetMap[marker] = cast(JournalTargetType, name)
            elif name in effectTypes:
                # Duplicates not allowed among effect types
                if marker in self.effectMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.effectMap[marker]}'."
                    )

                # Map markers to entry types
                self.effectMap[marker] = cast(JournalEffectType, name)

            elif name in effectModifierTypes:
                # Duplicates not allowed among effect types
                if marker in self.effectModMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.effectModMap[marker]}'."
                    )

                # Map markers to entry types
                self.effectModMap[marker] = cast(
                    JournalEffectModifier,
                    name
                )

            # else ignore it since it's an info type

    def markers(self) -> List[str]:
        """
        Returns the list of all entry-type markers (but not other kinds
        of markers), sorted from longest to shortest to help avoid
        ambiguities when matching.
        """
        entryTypes = get_args(JournalEntryType)
        return sorted(
            (
                m
                for (et, m) in self.formatDict.items()
                if et in entryTypes
            ),
            key=lambda m: -len(m)
        )

    def markerFor(self, markerType: JournalMarkerType) -> str:
        """
        Returns the marker for the specified entry/info/effect/etc.
        type.
        """
        return self.formatDict[markerType]

    def determineEntryType(self, entry: str) -> Tuple[
        JournalEntryType,
        Union[None, JournalTargetType, int],
        str
    ]:
        """
        Given a single line from a journal, returns a tuple containing
        the entry type for that line, the target part for that line, and
        a string containing the entry content (which is just the line
        minus the entry-type-and-target-marker). If no target type was
        included, the second entry of the return value will be `None`,
        and in the special case of zones, it will be an integer
        indicating the hierarchy level according to how many times the
        'zonePart' target specifier was present, default 0.

        Note that all spacing in the journal entry is reduced to single
        spaces in the return value.
        """
        # Get entry specifier
        bits = entry.strip().split()
        entrySpecifier = bits[0]
        remainder = ' '.join(bits[1:])

        # Figure out entry type from first character
        typeSpecifier = entrySpecifier[0]
        if typeSpecifier not in self.entryMap:
            raise JournalParseError(
                f"Entry does not begin with a recognized entry"
                f" marker:\n{entry}"
            )
        entryType = self.entryMap[typeSpecifier]

        # Figure out the entry target from second+ character(s)
        targetSpecifiers = entrySpecifier[1:]
        entryTarget: Union[None, JournalTargetType, int] = None
        if entryType == 'zone':
            specifiers = set(targetSpecifiers)
            if len(specifiers) > 0 and specifiers != {'z'}:
                raise JournalParseError(
                    f"Invalid target specifier for zone:\n{entry}"
                )
            entryTarget = len(targetSpecifiers)
        elif len(targetSpecifiers) > 0:
            if len(targetSpecifiers) > 1:
                raise JournalParseError(
                    f"Entry has too many target specifiers:\n{entry}"
                )
            elif targetSpecifiers not in self.targetMap:
                raise JournalParseError(
                    f"Unrecognized target specifier:\n{entry}"
                )
            entryTarget = self.targetMap[targetSpecifiers]
        # else entryTarget remains None

        return (entryType, entryTarget, remainder)

    def parseSpecificTransition(
        self,
        content: str
    ) -> Tuple[core.Decision, core.Transition]:
        """
        Splits a decision:transition pair to the decision and transition
        part, using a custom separator if one is defined.
        """
        sep = self.formatDict['transitionAtDecision']
        n = content.count(sep)
        if n == 0:
            raise JournalParseError(
                f"Cannot split '{content}' into a decision name and a"
                f" transition name (no separator '{sep}' found)."
            )
        elif n > 1:
            raise JournalParseError(
                f"Cannot split '{content}' into a decision name and a"
                f" transition name (too many ({n}) '{sep}' separators"
                f" found)."
            )
        else:
            return cast(
                Tuple[core.Decision, core.Transition],
                tuple(content.split(sep))
            )

    def splitDirections(
        self,
        content: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Splits a piece of text using the 'reciprocalSeparator' into two
        pieces. If there is no separator, the second piece will be
        `None`; if either side of the separator is blank, that side will
        be `None`, and if there is more than one separator, a
        `JournalParseError` will be raised. Whitespace will be stripped
        from both sides of each result.

        Examples:

        >>> pf = ParseFormat()
        >>> pf.splitDirections('abc / def')
        ('abc', 'def')
        >>> pf.splitDirections('abc def ')
        ('abc def', None)
        >>> pf.splitDirections('abc def /')
        ('abc def', None)
        >>> pf.splitDirections('/abc def')
        (None, 'abc def')
        >>> pf.splitDirections('a/b/c') # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
          ...
        JournalParseError: ...
        """
        sep = self.formatDict['reciprocalSeparator']
        count = content.count(sep)
        if count > 1:
            raise JournalParseError(
                f"Too many split points ('{sep}') in content:"
                f" '{content}' (only one is allowed)."
            )

        elif count == 1:
            before, after = content.split(sep)
            before = before.strip()
            after = after.strip()
            return (before or None, after or None)

        else: # no split points
            stripped = content.strip()
            if stripped:
                return stripped, None
            else:
                return None, None

    def parseItem(
        self,
        item: str
    ) -> Union[core.Power, Tuple[core.Token, int]]:
        """
        Parses an item, which is either a power (just a string) or a
        token-type:number pair (returned as a tuple with the number
        converted to an integer). The 'tokenQuantity' format value
        determines the separator which indicates a token instead of a
        power.
        """
        sep = self.formatDict['tokenQuantity']
        if sep in item:
            # It's a token w/ an associated count
            parts = item.split(sep)
            if len(parts) != 2:
                raise JournalParseError(
                    f"Item '{item}' has a '{sep}' but doesn't separate"
                    f" into a token type and a count."
                )
            typ, count = parts
            try:
                num = int(count)
            except ValueError:
                raise JournalParseError(
                    f"Item '{item}' has invalid token count '{count}'."
                )

            return (typ, num)
        else:
            # It's just a power
            return item

    def effectType(self, effectMarker: str) -> Optional[JournalEffectType]:
        """
        Returns the `JournalEffectType` string corresponding to the
        given effect marker string. Returns `None` for an unrecognized
        marker.
        """
        return self.effectMap.get(effectMarker)

    def effectModifier(
        self,
        arg: str
    ) -> Optional[Tuple[JournalEffectModifier, int]]:
        """
        Given an effect argument, determines whether or not it's an
        effect modifier. If it is not, it returns `None`. If it is a
        modifier, it returns a tuple containing the modifier type (one
        of the `JournalEffectModifier` strings) and the modifier value
        (an integer).
        """
        # Iterate through possibilities from longest to shortest to
        # avoid a shorter key which is a prefix of a longer key from
        # stealing values:
        for key in sorted(self.effectModMap, key=lambda x: -len(x)):
            # If arg starts with a key, it's a modifier
            if arg.startswith(key):
                modType = self.effectModMap[key]
                try:
                    modValue = int(arg[len(key):])
                except ValueError:
                    raise JournalParseError(
                        f"An effect modifier must consist of a modifier"
                        f" marker plus an integer. The argument {arg}"
                        f" starts with '{key}' but the rest of it is"
                        f" not an integer."
                    )
                return modType, modValue

        return None

    def parseEffect(self, effectString: str) -> core.TransitionEffect:
        """
        Given a strings specifying an effect, returns the
        `TransitionEffect` object that it specifies.
        """

        # Split into pieces
        pieces = effectString.split()
        if len(pieces) == 0:
            raise JournalParseError(
                "Effect must include at least a type."
            )

        # Get the effect type
        fType = self.effectType(pieces[0])

        if fType is None:
            raise JournalParseError(
                f"Unrecognized effect type {pieces[0]}. Check the"
                f" JournalEffectType entries in the format dictionary."
            )

        # Default result
        result: core.TransitionEffect = {
            'type': fType,
            'value': None,  # likely invalid for the specific type
            'delay': None,
            'charges': None
        }

        # Process delay and charge modifiers at any point among the
        # arguments.
        cleanArgs = []
        seen: Dict[JournalEffectModifier, str] = {}
        for arg in pieces[1:]:
            mod = self.effectModifier(arg)
            if mod is not None:
                modType, value = mod
                # Warn about duplicate modifiers
                if modType in seen:
                    warnings.warn(
                        (
                            f"Got multiple values for '{modType}':"
                            f" {seen[modType]!r} and {arg!r}. Only the"
                            f" last one will apply."
                        ),
                        JournalParseWarning
                    )
                seen[modType] = arg
                result[modType] = value
            else:
                cleanArgs.append(arg)

        if fType in ("gain", "lose"):
            if len(cleanArgs) != 1:
                raise JournalParseError(
                    f"'{fType}' effect must have exactly one argument (got"
                    f" {len(cleanArgs)}."
                )
            result['value'] = self.parseItem(cleanArgs[0])

        elif fType == "toggle":
            items = [self.parseItem(arg) for arg in cleanArgs]
            if any(not isinstance(item, core.Power) for item in items):
                raise JournalParseError(
                    "Only powers may be toggled, not tokens."
                )
            result['value'] = cast(List[core.Power], items)

        elif fType == "deactivate":
            if len(cleanArgs) != 0:
                raise JournalParseError(
                    f"A 'deactivate' effect may not include any"
                    f" arguments (got {len(cleanArgs)})."
                )

        elif fType == "edit":
            raise NotImplementedError(
                "edit effects are not implemented yet."
            )

        return result

    def removeComments(self, text):
        """
        Given a single line from a journal, removes all comments from it.
        Any '#' and any following characters through the end of a line
        counts as a comment.

        Returns the text without comments.
        """
        return self.commentRE.sub('', text)

    def blockEnd(self, string, startIndex):
        """
        Given a string and a start index where a block open delimiter
        is, returns the index within the string of the matching block
        closing delimiter.

        TODO: Under what conditions are delimiters ignored?
        """
        # TODO: HERE
        raise NotImplementedError()


#-------------------#
# Errors & Warnings #
#-------------------#

class JournalParseError(ValueError):
    """
    Represents a error encountered when parsing a journal.
    """
    pass


class JournalParseWarning(Warning):
    """
    Represents a warning encountered when parsing a journal.
    """
    pass


class PathEllipsis:
    """
    Represents part of a path which has been omitted from a journal and
    which should therefore be inferred.
    """
    pass


#-----------------#
# Parsing manager #
#-----------------#

class JournalObserver:
    """
    Keeps track of extra state needed when parsing a journal in order to
    produce a `core.Exploration` object. The methods of this class act
    as an API for constructing explorations that have several special
    properties. The API is designed to allow journal entries (which
    represent specific observations/events during an exploration) to be
    directly accumulated into an exploration object, including entries
    which apply to things like the most-recent-decision or -transition.

    You can use the `convertJournal` function to handle things instead,
    since that function creates and manages a `JournalObserver` object
    for you.

    The basic usage is as follows:

    1. Create a `JournalObserver`, optionally specifying a custom
        `ParseFormat`.
    2. Repeatedly either:
        * Call `record*` API methods corresponding to specific entries
            observed or...
        * Call `JournalObserver.observe` to parse one or more
            journal blocks from a string and call the appropriate
            methods automatically.
    3. Call `JournalObserver.getExploration` to retrieve the
        `core.Exploration` object that's been created.

    You can just call `convertJournal` to do all of these things at
    once.

    Notes:

    - `JournalObserver.getExploration` may be called at any time to get
        the exploration object constructed so far, and that that object
        (unless it's `None`) will always be the same object (which gets
        modified as entries are recorded). Modifying this object
        directly is possible for making changes not available via the
        API, but must be done carefully, as there are important
        conventions around things like decision names that must be
        respected if the API functions need to keep working.
    - To get the latest graph, simply use the
        `core.Exploration.currentGraph` method of the
        `JournalObserver.getExploration` result.

    ## Example

    >>> obs = JournalObserver()
    >>> e = obs.getExploration()
    >>> len(e) # blank starting state
    1
    >>> e.getPositionAtStep(0) # position is None before starting
    >>> # We start by using the record* methods...
    >>> obs.recordStart("Start")
    >>> obs.recordObserve("bottom")
    >>> len(e) # blank + started states
    2
    >>> e.positionAtStep(1)
    'Start'
    >>> obs.recordExplore("left", "West", "right")
    >>> len(e) # starting states + one step
    3
    >>> e.positionAtStep(1)
    'Start'
    >>> e.transitionAtStep(1)
    'left'
    >>> e.positionAtStep(2)
    'West'
    >>> obs.recordRetrace("right")
    >>> len(e) # starting states + two steps
    4
    >>> e.positionAtStep(1)
    'Start'
    >>> e.transitionAtStep(1)
    'left'
    >>> e.positionAtStep(2)
    'West'
    >>> e.transitionAtStep(2)
    'right'
    >>> e.positionAtStep(3)
    'Start'
    >>> obs.recordRetrace("bad") # transition doesn't exist
    Traceback (most recent call last):
    ...
    exploration.core.MissingTransitionError...
    >>> obs.recordObserve('right', 'East', 'left')
    >>> e.currentGraph().getTransitionRequirement('Start', 'right')
    ReqNothing()
    >>> obs.recordRequirement('crawl|small')
    >>> e.currentGraph().getTransitionRequirement('Start', 'right')
    ReqAny([ReqPower('crawl'), ReqPower('small')])
    >>> # The use of relative mode to add remote observations
    >>> obs.relative('East')
    >>> obs.recordObserve('top_vent')
    >>> obs.recordRequirement('crawl')
    >>> obs.recordReciprocalRequirement('crawl')
    >>> obs.recordExplore('right_door', 'Outside', 'left_door')
    >>> obs.recordRequirement('X')
    >>> obs.recordReciprocalRequirement('X')
    >>> obs.recordAction('lever') # no info on what it does yet...
    >>> # TODO door-toggling lever example
    >>> obs.relative() # leave relative mode
    >>> len(e) # starting states + two steps, no steps happen in relative mode
    4
    >>> g = e.currentGraph()
    >>> g.getTransitionRequirement(
    ...     g.getDestination('East', 'top_vent'),
    ...     'return'
    ... )
    ReqPower('crawl')
    >>> g.getTransitionRequirement('East', 'top_vent')
    ReqPower('crawl')
    >>> g.getTransitionRequirement('East', 'right_door')
    ReqImpossible()
    >>> g.getTransitionRequirement('Outside', 'left_door')
    ReqImpossible()
    >>> # Now we demonstrate the use of "observe"
    >>> obs.observe("o up Attic down\\nx up\\no vent\\nq crawl")
    >>> e.currentPosition()
    'Attic'
    >>> g = e.currentGraph()
    >>> g.getTransitionRequirement('Attic', 'vent')
    ReqPower('crawl')
    >>> sorted(list(g.destinationsFrom('Attic').items()))
    [('down', 'Start'), ('vent', '_u.6')]
    >>> obs.observe("a getCrawl\\nAt gain crawl\\nR vent East top_vent")
    >>> g = e.currentGraph()
    >>> g.getTransitionRequirement('East', 'top_vent')
    ReqPower('crawl')
    >>> g.getDestination('Attic', 'vent')
    'East'
    >>> g.getDestination('East', 'top_vent')
    'Attic'
    >>> len(e) # exploration, action, and return are each 1
    7
    >>> e.positionAtStep(3)
    'Start'
    >>> e.transitionAtStep(3)
    'up'
    >>> e.positionAtStep(4)
    'Attic'
    >>> e.transitionAtStep(4)
    'getCrawl'
    >>> e.positionAtStep(5)
    'Attic'
    >>> e.transitionAtStep(5)
    'vent'
    >>> e.positionAtStep(6)
    'East'
    """
    parseFormat: ParseFormat = ParseFormat()
    """
    The parse format used to parse entries supplied as text. This also
    ends up controlling some of the decision and transition naming
    conventions that are followed, so it is not safe to change it
    mid-journal; it should be set once before observation begins, and
    may be accessed but should not be changed.
    """

    exploration: core.Exploration
    """
    This is the exploration object being built via journal observations.
    Note that the exploration object may be empty (i.e., have length 0)
    even after the first few entries have been recorded because in some
    cases entries are ambiguous and are not translated into exploration
    steps until a further entry resolves that ambiguity.
    """

    def __init__(self, parseFormat: Optional[ParseFormat] = None):
        """
        Sets up the observer. If a parse format is supplied, that will
        be used instead of the default parse format, which is just the
        result of creating a `ParseFormat` with default arguments.
        """
        if parseFormat is None:
            self.parseFormat = ParseFormat()
        else:
            self.parseFormat = parseFormat

        # Create a blank exploration
        self.exploration = core.Exploration()

        # State variables

        # Tracks the most-recent transition so that things which apply to
        # a transition can be applied. Note that the current position is
        # just tracked via the `Exploration` object. This value is either
        # None or a pair including a decision and a transition name at
        # that decision.
        self.currentTransition: Optional[
            Tuple[core.Decision, core.Transition]
        ] = None

        # Stored decision/transition values that can be restored as the
        # current decision/transition later. This is used to support
        # relative mode.
        self.storedTransition: Optional[
            Tuple[core.Decision, core.Transition]
        ] = None

        # Whether or not we're in relative mode.
        self.inRelativeMode = False

        # Decision/transition values that are currently being targeted
        # in relative mode.
        self.targetDecision: Optional[core.Decision] = None
        self.targetTransition: Optional[
            Tuple[core.Decision, core.Transition]
        ] = None

        # A list of zones to be applied to decisions (level 0) or other
        # zones (levels 1+) whenever those things are created. If an
        # entry is `None`, then new zones/decisions in the level below
        # will not be added to any zone upon creation.
        self.zoneHierarchy: List[Optional[core.Zone]] = []

    def getExploration(self) -> core.Exploration:
        """
        Returns the exploration that this observer edits.
        """
        return self.exploration

    def currentDecisionTarget(self) -> Optional[core.Decision]:
        """
        Returns the decision which decision-based changes should be
        applied to. Changes depending on whether relative mode is
        active. Will be `None` when there is no current position (e.g.,
        before the exploration is started).
        """
        if self.inRelativeMode:
            return self.targetDecision
        else:
            return self.exploration.currentPosition()

    def definiteDecisionTarget(self) -> core.Decision:
        """
        Works like `currentDecisionTarget` but raises a
        `core.MissingDecisionError` instead of returning `None` if there
        is no current decision.
        """
        if self.inRelativeMode:
            result = self.targetDecision
        else:
            result = self.exploration.currentPosition()

        if result is None:
            raise core.MissingDecisionError(
                "There is no current decision."
            )
        else:
            return result

    def currentTransitionTarget(
        self
    ) -> Optional[Tuple[core.Decision, core.Transition]]:
        """
        Returns the decision, transition pair that identifies the current
        transition which transition-based changes should apply to. Will
        be `None` when there is no current transition (e.g., just after a
        warp).
        """
        if self.inRelativeMode:
            return self.targetTransition
        else:
            return self.currentTransition

    def currentReciprocalTarget(
        self
    ) -> Optional[Tuple[core.Decision, core.Transition]]:
        """
        Returns the decision, transition pair that identifies the
        reciprocal of the `currentTransitionTarget`. Will be `None` when
        there is no current transition, or when the current transition
        doesn't have a reciprocal (e.g., after an ending).
        """
        # relative mode is handled by `currentTransitionTarget`
        target = self.currentTransitionTarget()
        if target is None:
            return None
        now = self.exploration.currentGraph()
        return now.getReciprocalPair(*target)

    def checkFormat(
        self,
        entryType: str,
        target: Union[None, JournalTargetType, int],
        content: str,
        expectedTargets: Union[
            None,
            type[int],
            Collection[
                Union[None, JournalTargetType, int]
            ]
        ],
        expectedPieces: Union[None, int, Collection[int]]
    ) -> List[str]:
        """
        Does format checking for a journal entry after
        `determineEntryType` is called. Checks that the target is one
        from an allowed list of targets (or is `None` if
        `expectedTargets` is set to `None`) and that the number of
        pieces of content after calling split is a specific number or
        within a specific collection of allowed numbers.

        Returns the split-up content pieces, and raises a
        `JournalParseError` if its expectations are violated.
        """
        if expectedTargets is None:
            if target is not None:
                raise JournalParseError(
                    f"{entryType} entry may not specify a target."
                )
        elif expectedTargets is int:
            if not isinstance(target, int):
                raise JournalParseError(
                    f"{entryType} entry must have an integer target."
                )
        elif target not in cast(
            Collection[
                Union[None, JournalTargetType, int]
            ],
            expectedTargets
        ):
            raise JournalParseError(
                f"{entryType} entry had invalid target '{target}'."
            )

        pieces = content.split()
        if expectedPieces is None:
            # No restriction
            pass
        elif isinstance(expectedPieces, int):
            if len(pieces) != expectedPieces:
                raise JournalParseError(
                    f"{entryType} entry had {len(pieces)} arguments but"
                    f" only {expectedPieces} argument(s) is/are allowed."
                )

        elif len(pieces) not in expectedPieces:
            allowed = ', '.join(str(x) for x in expectedPieces)
            raise JournalParseError(
                f"{entryType} entry had {len(pieces)} arguments but the"
                f" allowed argument counts are: {allowed}"
            )

        return pieces

    def observe(self, journalText: str) -> None:
        """
        Ingests one or more journal blocks in text format (as a
        multi-line string) and updates the exploration being built by
        this observer, as well as updating internal state.

        This method can be called multiple times to process a longer
        journal incrementally including line-by-line.

        ## Example:

        >>> obs = JournalObserver()
        >>> obs.observe('''\\
        ... z Room1
        ... S start
        ... o nope
        ...   q power|tokens*3
        ... o unexplored
        ... o onwards
        ... x onwards sub_room backwards
        ... r backwards
        ... o down
        ...
        ... z Room2
        ... x down room2 up
        ... a box
        ...   At deactivate
        ...   At gain tokens*1
        ... o left
        ... o right
        ...   tt blue
        ...
        ... z Room3
        ... x right room3 left
        ... o right
        ... a miniboss
        ...   At deactivate
        ...   At gain power
        ... x right - left
        ... o ledge
        ...   q tall
        ... r left
        ... r left
        ... r up
        ...
        ... x nope secret back
        ... ''')
        >>> e = obs.getExploration()
        >>> len(e)
        13
        >>> m = e.currentGraph()
        >>> len(m)
        9
        >>> def showDestinations(m, r):
        ...     d = m.destinationsFrom(r)
        ...     for outgoing in sorted(d):
        ...         req = m.getTransitionRequirement(r, outgoing)
        ...         if req is None or req == core.ReqNothing():
        ...             req = ''
        ...         else:
        ...             req = ' {' + repr(req) + '}'
        ...         print(outgoing, d[outgoing] + req)
        ...
        >>> showDestinations(m, "start")
        down room2
        nope secret {ReqAny([ReqPower('power'), ReqTokens('tokens', 3)])}
        onwards sub_room
        unexplored _u.1
        >>> showDestinations(m, "secret")
        back start
        >>> showDestinations(m, "sub_room")
        backwards start
        >>> showDestinations(m, "room2")
        box room2 {ReqImpossible()}
        left _u.4
        right room3
        up start
        >>> m.transitionTags("room2", "right")
        {'blue'}
        >>> showDestinations(m, "room3")
        left room2
        miniboss room3 {ReqImpossible()}
        right -
        >>> showDestinations(m, "-")
        ledge _u.7 {ReqPower('tall')}
        left room3
        >>> showDestinations(m, "_u.7")
        return -
        >>> e.currentPosition()
        'secret'

        Note that there are plenty of other annotations not shown in
        this example; see `DEFAULT_FORMAT` for the default mapping from
        journal entry types to markers, and see `JournalEntryType` for
        the explanation for each entry type.

        Most entries start with a marker (which includes one character
        for the type and possibly one for the target) followed by a
        single space, and everything after that is the content of the
        entry.
        """
        # Normalize newlines
        journalText = journalText\
            .replace('\r\n', '\n')\
            .replace('\n\r', '\n')\
            .replace('\r', '\n')

        # Shortcut variable
        pf = self.parseFormat

        # Remove comments from entire text
        journalText = pf.removeComments(journalText)

        # Handle each line
        for line in journalText.splitlines():
            # Skip blank lines
            if line.strip() == '':
                continue

            eType, eTarget, eContent = pf.determineEntryType(line)
            if eType == 'START':
                pieces = self.checkFormat(
                    "START",
                    eTarget,
                    eContent,
                    None,
                    1
                )
                self.recordStart(*pieces)

            elif eType == 'explore':
                pieces = self.checkFormat(
                    "explore",
                    eTarget,
                    eContent,
                    None,
                    {1, 2, 3}
                )
                self.recordExplore(*pieces)

            elif eType == 'return':
                pieces = self.checkFormat(
                    "return",
                    eTarget,
                    eContent,
                    None,
                    {2, 3}
                )
                self.recordReturn(*pieces)

            elif eType == 'action':
                pieces = self.checkFormat(
                    "action",
                    eTarget,
                    eContent,
                    None,
                    1
                )
                self.recordAction(*pieces)

            elif eType == 'retrace':
                pieces = self.checkFormat(
                    "retrace",
                    eTarget,
                    eContent,
                    None,
                    1
                )
                self.recordRetrace(*pieces)

            elif eType == 'warp':
                pieces = self.checkFormat(
                    "warp",
                    eTarget,
                    eContent,
                    None,
                    1
                )
                self.recordWarp(*pieces)

            elif eType == 'wait':
                pieces = self.checkFormat(
                    "warp",
                    eTarget,
                    eContent,
                    None,
                    0
                )
                self.recordWait()

            elif eType == 'observe':
                pieces = self.checkFormat(
                    "observe",
                    eTarget,
                    eContent,
                    None,
                    (1, 2, 3)
                )
                self.recordObserve(*pieces)

            elif eType == 'END':
                pieces = self.checkFormat(
                    "END",
                    eTarget,
                    eContent,
                    None,
                    1
                )
                self.recordEnd(*pieces)

            elif eType == 'requirement':
                _ = self.checkFormat(
                    "requirement",
                    eTarget,
                    eContent,
                    (None, 'reciprocalPart'),
                    None
                )
                req = core.Requirement.parse(eContent)
                if eTarget == 'reciprocalPart':
                    self.recordReciprocalRequirement(req)
                else:
                    self.recordRequirement(req)

            elif eType == 'effect':
                _ = self.checkFormat(
                    "effect",
                    eTarget,
                    eContent,
                    None,
                    None
                )

                # TODO: Multi-line edit effects.... :(
                effect: core.TransitionEffect = pf.parseEffect(eContent)

                self.recordTransitionEffect(effect)

            elif eType == 'apply':
                _ = self.checkFormat(
                    "apply",
                    eTarget,
                    eContent,
                    (None, 'transitionPart'),
                    None
                )

                # TODO: Multi-line edit effects.... :(
                toApply: core.TransitionEffect = pf.parseEffect(eContent)

                # Apply the effect
                self.exploration.applyEffectNow(
                    toApply,
                    self.currentTransition
                )

                # If we targeted a transition, that means we wanted to
                # both apply the effect now AND set it up as an effect
                # of the transition we just took.
                if eTarget == 'transitionPart':
                    self.recordTransitionEffect(toApply)

            elif eType == 'tag':
                pieces = self.checkFormat(
                    "tag",
                    eTarget,
                    eContent,
                    (None, 'transitionPart', 'reciprocalPart'),
                    None
                )
                if len(pieces) == 0:
                    raise JournalParseError(
                        "tag entry must include at least one tag."
                    )
                if eTarget is None:
                    self.recordTagDecision(*pieces)
                elif eTarget == "transitionPart":
                    self.recordTagTranstion(*pieces)
                elif eTarget == "reciprocalPart":
                    self.recordTagReciprocal(*pieces)
                else:
                    raise JournalParseError(
                        f"Invalid tag target type '{eTarget}'."
                    )

            elif eType == 'annotate':
                pieces = self.checkFormat(
                    "annotate",
                    eTarget,
                    eContent,
                    (None, 'transitionPart', 'reciprocalPart'),
                    None
                )
                if len(pieces) == 0:
                    raise JournalParseError(
                        "annotation may not be empty."
                    )
                if eTarget is None:
                    self.recordAnnotateDecision(' '.join(pieces))
                elif eTarget == "transitionPart":
                    self.recordAnnotateTranstion(' '.join(pieces))
                elif eTarget == "reciprocalPart":
                    self.recordAnnotateReciprocal(' '.join(pieces))
                else:
                    raise JournalParseError(
                        f"Invalid annotation target type '{eTarget}'."
                    )

            elif eType == 'zone':
                pieces = self.checkFormat(
                    "zone",
                    eTarget,
                    eContent,
                    int,
                    (0, 1)
                )
                if eTarget is None:
                    eTarget = 0
                self.recordZone(
                    cast(int, eTarget),
                    pieces[0] if len(pieces) > 0 else None
                )

            elif eType == 'unify':
                pieces = self.checkFormat(
                    "unify",
                    eTarget,
                    eContent,
                    (None, 'transitionPart', 'reciprocalPart'),
                    (1, 2)
                )
                if eTarget is None:
                    self.recordUnify(*pieces)
                elif eTarget == 'transitionPart':
                    if len(pieces) != 1:
                        raise JournalParseError(
                            "A transition unification entry may only"
                            f" have one argument, but we got"
                            f" {len(pieces)}."
                        )
                    self.recordUnifyTransition(pieces[0])
                elif eTarget == 'reciprocalPart':
                    if len(pieces) != 1:
                        raise JournalParseError(
                            "A transition unification entry may only"
                            f" have one argument, but we got"
                            f" {len(pieces)}."
                        )
                    self.recordUnifyReciprocal(pieces[0])
                else:
                    raise RuntimeError(
                        f"Invalid target type {eTarget} after check for"
                        " unify entry!"
                    )

            elif eType == 'obviate':
                pieces = self.checkFormat(
                    "obviate",
                    eTarget,
                    eContent,
                    None,
                    2
                )
                transition, target = pieces
                targetDecision, targetTransition = (
                    pf.parseSpecificTransition(target)
                )
                self.recordObviate(
                    transition,
                    targetDecision,
                    targetTransition
                )

            elif eType == 'relative':
                pieces = self.checkFormat(
                    "relative",
                    eTarget,
                    eContent,
                    None,
                    (0, 1, 2)
                )
                try:
                    self.relative(*pieces)
                except core.BadStart:
                    raise JournalParseError(
                        "You cannot enter relative mode before the"
                        " 'start' entry."
                    )

            else:
                raise NotImplementedError(
                    f"Unrecognized event type '{eType}'."
                )

    def adjustZoneHierarchy(self, destination):
        """
        When moving to a new decision, if that decision is not in the
        same zone as the current zone hierarchy would add new decisions
        to, we reset the zone hierarchy to match the lineage of the
        destination. This function performs checks and then implements
        that.
        """
        # If the destination is not in the current bottom-of-hierarchy
        # zone, we replace the entire zone hierarchy with the
        # destination's zone lineage
        now = self.exploration.currentGraph()
        directs = sorted(
            now.allDirectZones(destination),
            key=lambda z: (now.zoneHierarchyLevel(z), z)
        )
        if (
            len(self.zoneHierarchy) == 0
         or self.zoneHierarchy[0] is None
        ):
            if len(directs) != 0:
                self.zoneHierarchy = cast(
                    List[Optional[core.Zone]],
                    now.zoneLineage(directs[0])
                )
            # otherwise we have a None/None match
        else:
            if self.zoneHierarchy[0] not in directs:
                if len(directs) > 0:
                    self.zoneHierarchy = cast(
                        List[Optional[core.Zone]],
                        now.zoneLineage(directs[0])
                    )
                else:
                    # Destination is not in any zones, so we empty
                    # the zone hierarchy
                    self.zoneHierarchy = []

            # Otherwise the destination zone matches

    def recordStart(self, name: core.Decision):
        """
        Records the start of the exploration. Use only once, as the very
        first entry (possibly after some zone declarations).

        To create new decision points that are disconnected from the rest
        of the graph, use the `relative` method.
        """
        if self.inRelativeMode:
            raise ValueError(
                "Can't start the exploration in relaive mode."
            )

        self.exploration.start(name, [])

        # Add the destination to our current zone if there is one
        if len(self.zoneHierarchy) > 0:
            zone = self.zoneHierarchy[0]
            if zone is not None:
                now = self.exploration.currentGraph()
                now.addDecisionToZone(name, zone)

    def recordObserve(
        self,
        name: core.Transition,
        destination: Optional[core.Decision] = None,
        reciprocal: Optional[core.Transition] = None
    ):
        """
        Records the observation of a new option at the current decision.

        If two or three arguments are given, the destination is still
        marked as unknown, but is given a name (with two arguments)
        and the reciprocal transition is named (with three arguments).
        """
        here = self.definiteDecisionTarget()
        self.exploration.observe(name, where=here)
        if self.inRelativeMode:
            self.targetTransition = (here, name)
        else:
            self.currentTransition = (here, name)

        # Rename the destination & reciprocal if names for them were
        # specified
        now = self.exploration.currentGraph()
        newUnknown = now.destination(here, name)

        if destination is not None:
            now.renameDecision(newUnknown, destination)
        else:
            destination = newUnknown

        if reciprocal is not None:
            now.addTransition(destination, reciprocal, here)
            now.mergeTransitions(
                destination,
                cast(core.Transition, now.getReciprocal(here, name)),
                reciprocal
            )

    def recordExplore(
        self,
        transition: core.Transition,
        destination: Optional[core.Decision] = None,
        reciprocal: Optional[core.Transition] = None
    ):
        """
        Records the exploration of a transition which leads to a
        specific destination. The name of the reciprocal transition may
        also be specified. Creates the transition if it needs to.

        If no destination name is specified, the destintion node must
        already exist and the name of the destination must not begin
        with '_u.' otherwise a `JournalParseError` will be generated.

        Sets the current transition to the transition taken.

        In relative mode, this makes all the same changes to the graph,
        without adding a new exploration step or applying transition
        effects.
        """
        here = self.definiteDecisionTarget()
        # Create transition if it doesn't already exist
        now = self.exploration.currentGraph()
        leadsTo = now.getDestination(here, transition)
        if leadsTo is None:
            if destination is None:
                raise JournalParseError(
                    f"Transition '{transition}' at decision '{here}'"
                    f" does not already exist, so a destination name"
                    f" must be provided."
                )
            else:
                now.addUnexploredEdge(here, transition)
        elif destination is None:
            # TODO: Generalize this...
            if leadsTo.startswith('_u.'):
                raise JournalParseError(
                    f"Destination '{leadsTo}' from decision '{here}'"
                    f" via transition '{transition}' must be named when"
                    f" explored, because it does not already have a"
                    f" name."
                )
            else:
                destination = leadsTo

        if self.inRelativeMode:
            now.replaceUnexplored(
                here,
                transition,
                destination,
                reciprocal
            )
            self.targetDecision = destination
            self.targetTransition = (here, transition)
        else:
            self.exploration.explore(
                transition,
                destination,
                [],
                reciprocal
            )
            self.currentTransition = (here, transition)

        # Add the destination to our current zone if there is one
        if len(self.zoneHierarchy) > 0:
            zone = self.zoneHierarchy[0]
            if zone is not None:
                now = self.exploration.currentGraph()
                now.addDecisionToZone(destination, zone)

    def recordRetrace(self, transition: core.Transition):
        """
        Records retracing a transition which leads to a known
        destination.

        Sets the current transition to the transition taken.

        In relative mode, simply sets the current transition target to
        the transition taken and sets the current decision target to its
        destination (it does not apply transition effects).
        """
        here = self.definiteDecisionTarget()
        if self.inRelativeMode:
            now = self.exploration.currentGraph()
            self.targetDecision = now.destination(here, transition)
            self.targetTransition = (here, transition)
        else:
            self.exploration.retrace(transition)
            self.currentTransition = (here, transition)

        # Adjust the zone hierarchy if necessary
        self.adjustZoneHierarchy(self.exploration.currentPosition())

    def recordAction(self, name: core.Transition):
        """
        Records an action taken at the current decision. If a transition
        of that name already existed, it will be converted into an action
        assuming that its destination is unexplored and has no
        connections yet, and that its recirocal also has no special
        properties yet. If those assumptions do not hold, a
        `JournalParseError` will be raised under the assumption that the
        name collision was an accident, not intentional, since the
        destination and reciprocal are deleted in the process of
        converting a normal transition into an action.

        In relative mode, the action is created (or the transition is
        converted into an action) but effects are not applied.

        Example:

        >>> o = JournalObserver()
        >>> e = o.getExploration()
        >>> o.recordStart('start')
        >>> o.recordObserve('transition')
        >>> e.currentState().get('powers', set())
        set()
        >>> o.recordObserve('action') # not noted as an action yet...
        >>> # TODO: 'oa' syntax for this?
        >>> o.recordTransitionEffect(
        ...     {
        ...         'type': 'gain',
        ...         'value': 'power',
        ...         'charges': None,
        ...         'delay': None
        ...     }
        ... )
        >>> o.recordAction('action') # turns it into an action
        >>> e.currentState().get('powers', set())
        {'power'}
        >>> o.recordAction('another') # add effects after...
        >>> effect = {
        ...         'type': 'lose',
        ...         'value': 'power',
        ...         'charges': None,
        ...         'delay': None
        ... }
        >>> # These lines apply the effect and then add it to the
        >>> # transition, since we alread took the transition
        >>> e.applyEffectNow(effect, o.currentTransition)
        >>> o.recordTransitionEffect(effect)
        >>> e.currentState()['powers']
        set()
        >>> len(e)
        4
        >>> e.getPositionAtStep(0)
        >>> e.positionAtStep(1)
        'start'
        >>> e.positionAtStep(2)
        'start'
        >>> e.positionAtStep(3)
        'start'
        >>> e.transitionAtStep(0)
        '_START_'
        >>> e.transitionAtStep(1)
        'action'
        >>> e.transitionAtStep(2)
        'another'
        """
        here = self.definiteDecisionTarget()

        # Check if the transition already exists
        now = self.exploration.currentGraph()
        destinations = now.destinationsFrom(here)
        if name in destinations:
            destination = destinations[name]
            reciprocal = now.getReciprocal(here, name)
            # To replace a transition with an action, the transition may
            # only have outgoing properties. Otherwise we assume it's an
            # error to name the action after a transition which was
            # intended to be a real transition.
            if (
                not now.isUnknown(destination)
             or now.degree(destination) > 2
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its destination is already explored or has"
                    f" been connected to."
                )
            if (
                reciprocal is not None
            and now.getTransitionProperties(
                    destination,
                    reciprocal
                ) != {
                    'requirement': core.ReqNothing(),
                    'effects': [],
                    'tags': set(),
                    'annotations': []
                }
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its reciprocal has custom properties."
                )

            if (
                now.decisionAnnotations(destination) != []
             or now.decisionTags(destination) != {'unknown'}
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its destination has tags and/or annotations."
                )

            # If we get here, re-target the transition, and then destroy
            # the old destination along with the old reciprocal edge.
            now.retargetTransition(
                here,
                name,
                here,
                swapReciprocal=False
            )
            now.removeDecision(destination)

        # This will either take the existing action OR create it if
        # necessary
        if self.inRelativeMode:
            if name not in destinations:
                now.addAction(here, name)
            self.targetTransition = (here, name)
        else:
            self.exploration.takeAction(name)
            self.currentTransition = (here, name)

    def recordReturn(
        self,
        transition: core.Transition,
        destination: core.Decision,
        reciprocal: Optional[core.Transition] = None
    ):
        """
        Records an exploration which leads back to a
        previously-encountered decision. If a reciprocal is specified,
        we connect to that transition as our reciprocal (it must have
        led to an unknown area or not have existed) or if not, we make a
        new connection with an automatic reciprocal name.

        Sets the current transition to the transition taken.

        In relative mode, does the same stuff but doesn't apply any
        transition effects.
        """
        here = self.definiteDecisionTarget()
        now = self.exploration.currentGraph()
        if self.inRelativeMode:
            now.replaceUnexplored(
                here,
                transition,
                destination,
                reciprocal
            )
            self.targetDecision = destination
            self.targetTransition = (here, transition)
        else:
            self.exploration.returnTo(
                transition,
                destination,
                reciprocal
            )
            self.currentTransition = (here, transition)

        # Adjust the zone hierarchy if necessary
        self.adjustZoneHierarchy(destination)

    def recordWarp(self, destination: core.Decision):
        """
        Records a warp to a specific destination without creating a
        transition. If the destination did not exist, it will be
        created. If it gets created, the destination will be added to the
        current zone. However, if the destination already exists and is
        in a zone that's different from the current level-0 zone (or is
        NOT in a zone at all and the current level-0 zone is not None)
        then the entire current zone hierarchy will be replaced by the
        zone lineage of the destination's first direct zone, as ordered
        by zone hierarchy level and then zone name (see
        `exploration.core.DecisionGraph.zoneLineage`,
        `exploration.core.DecisionGraph.zoneHierarchyLevel`, and
        `exploration.core.DecisionGraph.allDirectZones`).

        TODO: What about gap compression in zone hierarchies...?

        Sets the current transition to `None`.

        In relative mode, simply updates the current target decision and
        sets the current target transition to `None`. It will still
        create the destination if necessary, but in relative mode, the
        destination is not marked as unknown (in normal mode it's marked
        as unknown in the step before the warp and known afterwards).
        """
        now = self.exploration.currentGraph()

        # Create the destination if it didn't exist already
        if destination not in now:
            now.addDecision(destination)
            if not self.inRelativeMode:
                now.setUnknown(destination)
                # The warp step will mark it as known in the next
                # exploration step, but in this one it's unknown.

            # Add it to our current zone if there is one
            if len(self.zoneHierarchy) > 0:
                zone = self.zoneHierarchy[0]
                if zone is not None:
                    now.addDecisionToZone(destination, zone)

        else:
            # Adjust the zone hierarchy if necessary
            self.adjustZoneHierarchy(destination)

        if self.inRelativeMode:
            self.targetDecision = destination
            self.targetTransition = None
        else:
            self.exploration.warp(destination)
            self.currentTransition = None

    def recordWait(self):
        """
        Records a wait step. Does not modify the current transition.

        Raises a `JournalParseError` in relative mode, since it wouldn't
        have any effect.
        """
        if self.inRelativeMode:
            raise JournalParseError("Can't wait in relative mode.")
        else:
            self.exploration.wait()

    def recordEnd(self, name: core.Decision):
        """
        Records an ending. Sets the current transition to the transition
        that leads to the ending. Endings are not added to zones, and
        they also don't affect the current zone hierarchy.

        Does the same thing in relative mode.
        """
        graph = self.exploration.currentGraph()
        here = self.definiteDecisionTarget()
        fullName = graph.addEnding(here, name)
        if self.inRelativeMode:
            self.targetDecision = fullName
            self.targetTransition = (here, fullName)
        else:
            self.exploration.retrace(fullName)
            self.currentTransition = (here, fullName)
        # TODO: Prevent things like adding unexplored nodes to the
        # ending...

    def recordRequirement(self, req: core.Requirement):
        """
        Records a requirement observed on the most recently
        defined/taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Can't set a requirement because there is no current"
                " transition."
            )
        self.exploration.currentGraph().setTransitionRequirement(
            *target,
            req
        )

    def recordReciprocalRequirement(self, req: core.Requirement):
        """
        Records a requirement observed on the reciprocal of the most
        recently defined/taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Can't set a reciprocal requirement because there is no"
                " current transition or it doesn't have a reciprocal."
            )
        graph = self.exploration.currentGraph()
        graph.setTransitionRequirement(*target, req)

    def recordTransitionEffect(
        self,
        effect: core.TransitionEffect
    ):
        """
        Records a transition effect, which is immediately added to any
        effects of the currently-relevant transition (the most-recently
        created or taken transition). A `JournalParseError` will be
        raised if there is no current transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot apply an effect because there is no current"
                " transition."
            )

        now = self.exploration.currentGraph()
        now.addTransitionEffect(*target, effect)

    def recordReciprocalEffect(
        self,
        effect: core.TransitionEffect
    ):
        """
        Like `recordTransitionEffect` but applies the effect to the
        reciprocal of the current transition. Will cause a
        `JournalParseError` if the current transition has no reciprocal
        (e.g., it's an ending transition).
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot apply a reciprocal effect because there is no"
                " current transition, or it doesn't have a reciprocal."
            )

        now = self.exploration.currentGraph()
        now.addTransitionEffect(*target, effect)

    def recordTagDecision(
        self,
        *tags: core.Tag
    ):
        """
        Records tags to be applied to the current decision.
        """
        now = self.exploration.currentGraph()
        now.tagDecision(self.definiteDecisionTarget(), set(tags))

    def recordTagTranstion(
        self,
        *tags: core.Tag
    ):
        """
        Records tags to be applied to the most-recently-defined or
        -taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot tag a transition because there is no current"
                " transition."
            )

        now = self.exploration.currentGraph()
        now.tagTransition(*target, set(tags))

    def recordTagReciprocal(
        self,
        *tags: core.Tag
    ):
        """
        Records tags to be applied to the reciprocal of the
        most-recently-defined or -taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot tag a transition because there is no current"
                " transition."
            )

        now = self.exploration.currentGraph()
        now.tagTransition(*target, set(tags))

    def recordAnnotateDecision(
        self,
        *annotations: core.Annotation
    ):
        """
        Records tags to be applied to the current decision.
        """
        now = self.exploration.currentGraph()
        now.annotateDecision(self.definiteDecisionTarget(), annotations)

    def recordAnnotateTranstion(
        self,
        *annotations: core.Annotation
    ):
        """
        Records tags to be applied to the most-recently-defined or
        -taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot annotate a transition because there is no"
                " current transition."
            )

        now = self.exploration.currentGraph()
        now.annotateTransition(*target, annotations)

    def recordAnnotateReciprocal(
        self,
        *annotations: core.Annotation
    ):
        """
        Records tags to be applied to the reciprocal of the
        most-recently-defined or -taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot annotate a reciprocal because there is no"
                " current transition or because it doens't have a"
                " reciprocal."
            )

        now = self.exploration.currentGraph()
        now.annotateTransition(*target, annotations)

    def recordZone(self, level: int, zone: Optional[core.Zone]):
        """
        Records a new current zone to be applied to all
        subsequently-created decisions (or zones) at a given hierarchy
        level, with level 0 applying directly to decisions, level 1
        applying to level-0 zones, level 2 applying to level-1 zones,
        etc. If `None` is specified, then that level of the hierarchy
        will be empty and lower-level zones (or decisions) will not be
        added to any zone upon creation. When there's a gap in the
        hierarchy, levels above the gap do NOT get zones below the gap
        added to them.
        """
        while len(self.zoneHierarchy) < level + 1:
            self.zoneHierarchy.append(None)
        self.zoneHierarchy[level] = zone

        now = self.exploration.currentGraph()

        if zone is not None:
            # Create the zone if it didn't already exist
            if not now.hasZone(zone):
                now.createZone(zone)

            # Add to the current zone in the level above if there is one
            if len(self.zoneHierarchy) >= level + 2:
                above = self.zoneHierarchy[level + 1]
                if above is not None:
                    now.addZoneToZone(zone, above)

    def recordUnify(
        self,
        merge: core.Decision,
        mergeInto: Optional[core.Decision] = None
    ):
        """
        Records a unification between two decisions. This marks an
        observation that they are actually the same decision and it
        merges them. If only one decision is given the current decision
        is merged into that one. After the merge, the first decision (or
        the current decision if only one was given) will no longer
        exist.

        If one of the merged decisions was the current position of the
        exploration, the merged decision will be the current position
        after the merge, and this happens even when in relative mode.
        In relative mode, the target decision is also updated if it
        needs to be.

        A `TransitionCollisionError` will be raised if the two decisions
        have outgoing transitions that share a name.

        Logs a `JournalParseWarning` if the two decisions were in
        different zones.
        """
        if mergeInto is None:
            mergeInto = merge
            merge = self.definiteDecisionTarget()

        now = self.exploration.currentGraph()
        now.mergeDecisions(merge, mergeInto)

        # Update current position if it was merged
        if self.exploration.currentPosition() == merge:
            self.exploration.positions[-1] = mergeInto

        # Update targets if they were merged
        if self.inRelativeMode:
            if self.targetDecision == merge:
                self.targetDecision = mergeInto
            if (
                self.targetTransition
            and self.targetTransition[0] == merge
            ):
                self.targetTransition = (
                    mergeInto,
                    self.targetTransition[1]
                )
        else:
            # Update current transition if it was merged
            if (
                self.currentTransition
            and self.currentTransition[0] == merge
            ):
                self.currentTransition = (
                    mergeInto,
                    self.currentTransition[1]
                )

        # Update stored decision/transition
        if self.storedTransition and self.storedTransition[0] == merge:
            self.storedTransition = (
                mergeInto,
                self.storedTransition[1]
            )

    def recordUnifyTransition(self, target: core.Transition):
        """
        Records a unification between the most-recently-defined or
        -taken transition and the specified transition (which must be
        outgoing from the same decision). This marks an observation that
        two transitions are actually the same transition and it merges
        them.

        After the merge, the target transition will still exist but the
        previously most-recent transition will have been deleted.

        Their reciprocals will also be merged.

        A `JournalParseError` is raised if there is no most-recent
        transition.
        """
        now = self.exploration.currentGraph()
        affected = self.currentTransitionTarget()
        if affected is None or affected[1] is None:
            raise JournalParseError(
                "Cannot unify transitions: there is no current"
                " transition."
            )

        decision, transition = affected

        # If they don't share a target, then the current transition must
        # lead to an unknown node, which we will dispose of
        destination = now.getDestination(decision, transition)
        if destination is None:
            raise JournalParseError(
                f"Cannot unify transitions: transition"
                f" '{transition}' at decision '{decision}' has no"
                f" destination."
            )

        finalDestination = now.getDestination(decision, target)
        if finalDestination is None:
            raise JournalParseError(
                f"Cannot unify transitions: transition"
                f" '{target}' at decision '{decision}' has no"
                f" destination."
            )

        if destination != finalDestination:
            if not now.isUnknown(destination):
                raise JournalParseError(
                    f"Cannot unify transitions: destination"
                    f" '{destination}' of transition '{transition}' at"
                    f" decision '{decision}' is not an unknown"
                    f" decision."
                )
            # Retarget and delete the unknown node that we abandon
            # TODO: Merge nodes instead?
            now.retargetTransition(
                decision,
                transition,
                finalDestination
            )
            now.removeDecision(destination)
            if self.targetDecision == destination:
                self.targetDecision = finalDestination
            # TODO: What if that destination was part of another target?

        # Now we can merge transitions
        now.mergeTransitions(decision, transition, target)

    def recordUnifyReciprocal(
        self,
        target: core.Transition
    ):
        """
        Records a unification between the reciprocal of the
        most-recently-defined or -taken transition and the specified
        transition, which must be outgoing from the current transition's
        destination. This marks an observation that two transitions are
        actually the same transition and it merges them, deleting the
        original reciprocal. Note that the current transition will also
        be merged with the reciprocal of the target.

        A `JournalParseError` is raised if there is no current
        transition, or if it does not have a reciprocal.
        """
        now = self.exploration.currentGraph()
        affected = self.currentReciprocalTarget()
        if affected is None or affected[1] is None:
            raise JournalParseError(
                "Cannot unify transitions: there is no current"
                " transition."
            )

        decision, transition = affected

        destination = now.destination(decision, transition)
        reciprocal = now.getReciprocal(decision, transition)
        if reciprocal is None:
            raise JournalParseError(
                "Cannot unify reciprocal: there is no reciprocal of the"
                " current transition."
            )

        # If they don't share a target, then the current transition must
        # lead to an unknown node, which we will dispose of
        finalDestination = now.getDestination(destination, target)
        if finalDestination is None:
            raise JournalParseError(
                f"Cannot unify reciprocal: transition"
                f" '{target}' at decision '{destination}' has no"
                f" destination."
            )

        if decision != finalDestination:
            if not now.isUnknown(decision):
                raise JournalParseError(
                    f"Cannot unify reciprocal: destination"
                    f" '{decision}' of transition '{reciprocal}' at"
                    f" decision '{destination}' is not an unknown"
                    f" decision."
                )
            # Retarget and delete the unknown node that we abandon
            # TODO: Merge nodes instead?
            now.retargetTransition(
                destination,
                reciprocal,
                finalDestination
            )
            now.removeDecision(decision)
            # TODO: Retargeting stuff!! HERE

        # Actually merge the transitions
        now.mergeTransitions(destination, reciprocal, target)

    def recordObviate(
        self,
        transition: core.Transition,
        otherDecision: core.Decision,
        otherTransition: core.Transition
    ):
        """
        Records the obviation of a transition at another decision. This
        is the observation that a specific transition at the current
        decision is the reciprocal of a different transition at another
        decision which previously led to an unknown area. The difference
        between this and `recordReturn` is that `recordReturn` logs
        movement across the newly-connected transition, while this
        leaves the player at their original decision (and does not even
        add a step to the current exploration).

        Both transitions will be created if they didn't already exist.

        In relative mode does the same thing but doesn't move the current
        decision across the transition updated.
        """
        now = self.exploration.currentGraph()
        here = self.definiteDecisionTarget()
        otherDestination = now.getDestination(
            otherDecision,
            otherTransition
        )
        if otherDestination is not None:
            if not now.isUnknown(otherDestination):
                raise JournalParseError(
                    f"Cannot obviate transition '{otherTransition}' at"
                    f" decision '{otherDecision}': that transition leads"
                    f" to decision '{otherDestination}' which is not an"
                    f" unknown decision."
                )
        else:
            # We must create the other destination
            now.addUnexploredEdge(otherDecision, otherTransition)

        destination = now.getDestination(here, transition)
        if destination is not None:
            if not now.isUnknown(destination):
                raise JournalParseError(
                    f"Cannot obviate using transition '{transition}' at"
                    f" decision '{here}': that transition leads to"
                    f" decision '{destination}' which is not an unknown"
                    f" decision."
                )
        else:
            # we need to create it
            now.addUnexploredEdge(here, transition)

        # Now connect the transitions and clean up the unknown nodes
        now.replaceUnexplored(
            here,
            transition,
            otherDecision,
            otherTransition
        )
        if self.inRelativeMode:
            self.targetTransition = (here, transition)
        else:
            self.currentTransition = (here, transition)

    def relative(
        self,
        where: Optional[core.Decision] = None,
        transition: Optional[core.Transition] = None,
    ) -> None:
        """
        Enters 'relative mode' where the exploration ceases to add new
        steps but edits can still be performed on the current graph. This
        also changes the current decision/transition settings so that
        edits can be applied anywhere. It can accept 0, 1, or 2
        arguments. With 0 arguments, it simply enters relative mode but
        maintains the current position as the target decision and the
        last-taken or last-created transition as the target transition
        (note that that transition usually originates at a different
        decision). With 1 argument, it sets the target decision to the
        decision named, and sets the target transition to None. With 2
        arguments, it sets the target decision to the decision named, and
        the target transition to the transition named, which must
        originate at that target decision.

        If given the name of a decision which does not yet exist, it will
        create that decision in the current graph, disconnected from the
        rest of the graph. In that case, it is an error to also supply a
        transition to target (you can use other commands once in relative
        mode to build more transitions and decisions out from the
        newly-created decision).

        When called in relative mode, it updates the current position
        and/or decision, or if called with no arguments, it exits
        relative mode. When exiting relative mode, the current decision
        is set back to the graph's current position, and the current
        transition is set to whatever it was before relative mode was
        entered.

        Raises a `TypeError` if a transition is specified without
        specifying a decision. Raises a `ValueError` if given no
        arguments and the exploration does not have a current position.
        Also raises a `ValueError` if told to target a specific
        transition which does not exist. Raises a `core.BadStart` error
        if called before the exploration is started.
        """
        if len(self.exploration.currentGraph()) == 0:
            raise core.BadStart(
                "Cannot enter relative mode before the exploration is"
                " started (call `recordStart` first)."
            )

        if where is None:
            if transition is not None:
                raise TypeError(
                    "Cannot specify a transition without also"
                    " specifying a decision."
                )
            if self.inRelativeMode:
                # If we're in relative mode, cancel it
                self.inRelativeMode = False

                # Here we restore saved sate
                self.currentTransition = self.storedTransition
                self.storedTransition = None
                self.targetTransition = None

            else:
                # Enter relative mode and set up the current
                # decision/transition as the targets

                # Store state
                self.storedTransition = self.currentTransition

                # Enter relative mode
                self.inRelativeMode = True

                # Set targets
                self.targetDecision = self.exploration.currentPosition()
                if self.targetDecision is None:
                    raise ValueError(
                        "Cannot enter relative mode at the current"
                        " position becuase there is no current"
                        " position."
                    )
                self.targetTransition = self.currentTransition

        else: # we have at least a decision to target
            # If we're entering relative mode instead of just changing
            # focus, we need to set up the targetTransition if no
            # transition was specified.
            if not self.inRelativeMode:
                # We'll be entering relative mode, so store state
                self.storedTransition = self.currentTransition
                if transition is None:
                    self.targetTransition = self.currentTransition

            # Enter (or stay in) relative mode
            self.inRelativeMode = True

            # Target the specified decision
            self.targetDecision = where

            # Target the specified transition
            now = self.exploration.currentGraph()
            if transition is not None:
                self.targetTransition = (where, transition)
                if now.getDestination(where, transition) is None:
                    raise ValueError(
                        f"Cannot target transition '{transition}' at"
                        f" decision '{where}': there is no such"
                        f" transition."
                    )
            # otherwise leave self.targetTransition alone

            # If we're targeting a previously non-existent decision,
            # create it.
            if self.targetDecision not in now:
                if transition is not None:
                    raise TypeError(
                        f"Cannot specify a target transition when"
                        f" entering relative mode at previously"
                        f" non-existent decision '{where}'."
                    )
                now.addDecision(self.targetDecision)


#--------------------#
# Shortcut Functions #
#--------------------#

def convertJournal(
    journal: str,
    format: Optional[ParseFormat] = None
) -> core.Exploration:
    """
    Converts a journal in text format into a `core.Exploration` object,
    using a fresh `JournalObserver`. An optional `ParseFormat` may be
    specified if the journal doesn't follow the default parse format.
    """
    obs = JournalObserver(format)
    obs.observe(journal)
    return obs.getExploration()
