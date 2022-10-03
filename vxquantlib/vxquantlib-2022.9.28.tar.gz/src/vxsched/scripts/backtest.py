class vxBacktestEngine:
    """回测引擎"""

    def _run_backtest(self, start_dt, end_dt):
        vxtime.backtest(start_dt, end_dt)
        logger.info("=" * 80)
        logger.info(
            f"========  回测开始:{to_timestring(start_dt)} 至 {to_timestring(end_dt)}  ========"
        )
        logger.info("=" * 80)
        while self._active and self._channel.next_trigger_dt is not None:
            sleep_time = self._channel.next_trigger_dt - vxtime.now()
            if sleep_time > 0:
                try:
                    vxtime.sleep(sleep_time)
                except StopIteration:
                    break

            event = self._channel.get(vxtime.now())

            if not event:
                continue

            if event.trigger and event.trigger.status != TriggerStatus.Completed:
                event.next_trigger_dt = next(event.trigger, None)
                self._channel.put(event)

            self._handlers.trigger(event)

        on_backtest_finished_event = vxEvent(type="on_backtest_finished")
        self._handlers.trigger(on_backtest_finished_event)
        logger.info("=" * 80)
        logger.info("========  回测结束  ========")
        logger.info("=" * 80)

    def _run_util_end_dt(self, end_dt: float) -> None:
        while self._active:
            now = vxtime.now()
            if now > end_dt:
                logger.info(f"已到达终止时间{to_timestring(end_dt)},退出运行...")
                break

            event = self._channel.get(now)
            if not event:
                continue

            if event.trigger and event.trigger.status != TriggerStatus.Completed:
                event.next_trigger_dt = next(event.trigger, None)
                self._channel.put(event)

            self._handlers.trigger(event)
