""" Simplest telegram bot """

import os
import time
from typing import Any
from requests import request
from .utils import command_parser
import subprocess as ps

class Bot:
    """ Simplest telegram bot """

    def __init__(self, token:str=None):

        if token is None and os.getenv('TELEGRAM_BOT_TOKEN') is None:
            raise ValueError('You have to either provide a token in the init method or define'
                             'an environmental variable `TELEGRAM_BOT_TOKEN`')
        self.token = os.getenv('TELEGRAM_BOT_TOKEN') if token is None else token

        # Prepare all urls that would be used so we don't have to do it in each method
        self.base_url = 'https://api.telegram.org/bot{token}/{method}'
        self.get_updates_url = self.base_url.format(token=self.token, method='getUpdates')
        self.send_message_url = self.base_url.format(token=self.token, method='sendMessage')
        self.__commands = {}

    def __make_request(self, request_method, url, **kwargs):
        """ Wrapper for Python requests method """
        return request(request_method, url, timeout=10, **kwargs)

    def __ack_message(self, msg) -> bool:
        """Acknoledges that the previos update has been received. The system works
        by sending last's message update_id and incrementing it by 1. The new value
        should be supplied to the offeset parameter in the entities array.

        Args:
            update_id (int): The update_id of the message we would like to acknowledge

        Raises:
            Exception: If HTTP status code is not 200

        Returns:
            bool: True if the previos message was acknoledged correctly
        """
        update_id = msg['update_id']

        payload = {'offset' : update_id + 1}
        res = self.__make_request('get', self.get_updates_url, data=payload)

        if res.status_code != 200:
            raise Exception('An error occured with message acknowledgement')
        return True

    def __cmd_registered(self, user_cmd:str) -> bool:
        """Checks if commands are registered

        Args:
            user_cmd (str): User command with the following syntax: /test

        Returns:
            bool: True if command is registered. False otherwise.
        """
        if self.__commands.get(user_cmd) is None:
            print(f'The supplied command "{user_cmd}" was not registered. '
                   'Message will be acknoledged but action not executed!')
            return False
        return True

    def __notify_sender(self, chat_id, msg):
        """ Wrapper function of send_msg (just for clarity)
        """
        return self.send_msg(chat_id, msg)

    def __execute_command(self, msg:dict[str, Any]) -> bool:
        """Executes a remote command provided via Telegram chat with the bot

        Args:
            msg (dict[str, Any]): Parsed telegram message from `__get_message(...)`

        Returns:
            bool: True if the command was executed successfully. False otherwise.
        """
        cmd = msg['message']['text']
        chat_id = msg['message']['chat']['id']

        if self.__cmd_registered(cmd):
            command = self.__commands.get(cmd)
            output = ps.run(command, capture_output=True, check=True, text=True)
            self.__notify_sender(chat_id, f'{cmd} executed successfully. Output is down below:\n\n'
            f'{output.stdout}')
            return True
        self.__notify_sender(chat_id, f'{cmd} was not executed because it is not registered. Please register.')
        return False

    def __get_message(self) -> dict:
        """Gets a single message from by polling.

        Note: If a message does not have entities array in the results, that might
        be due to the fact that the sent message is not a registered bot command.

        Returns:
            dict: Returns the last unacknowledged message
        """
        try:
            res = self.__make_request('get', self.get_updates_url)
            if res.json()['result']:
                return res.json()['result'][0]
        except Exception as err: # Better exception handling is required
            raise Exception from err

    def register_commands(self, file) -> dict[str, str]:
        """Registers a set of command for the bot to execute

        commands:
            1:
                name: Test command
                description: Test description
                command: /test
                action: Hi jordan
            2:
                name: Test command
                description: Test description
                command: /test1
                action: Hi jordan1
        Args:
            file (yaml): Yaml like file as described above

        Returns:
            dict[str, str]: Parsed dictionary
        """

        data = command_parser(file)
        self.__commands = data

    def send_msg(self, to:str, msg:str) -> bool:
        """A helper method that sends a message to particular telegram chat id.

        Args:
            to (str): A specific chat id where messages will be sent.
            msg (str): Message

        Raises:
            Exception: If response status code is different from 200, we raise an exception

        Returns:
            bool: Return true if the message was sent successfully
        """

        payload = {'chat_id' : to, 'text' : msg}
        res = self.__make_request('post', self.send_message_url, data=payload)

        if res.status_code != 200:
            raise Exception(f'An error occured with message notification - {res.status_code}')
        return True

    def listen(self, interval:int=3) -> None:
        """Main loop that polls messages for a particular bot as defined by the
        get_updates_url.

        The way Telegram's polling system works is by getting the last messages from
        getUpdates API. Once message is received you have to acknowledgement it,
        otherwise it will stay in the queue and the poll system will always return all messages
        until properly acknowledged. By design the polling system returns all messaages
        in a `results` array and you need to iterate over them one by one in order to read them.
        To avoid going over all messages at once, the __get_message API return only the first
        result from the array, guaranteeing that this is the first unacknoledged message from
        the queue.
        A message can be acknoledged after sending an updated update_id to getUpdates API.
        See self.__ack_message method

        Args:
            interval (int): Interval between each poll.
        """
        print('Bot started listening for updates...')
        try:
            while True:
                time.sleep(interval)
                msg = self.__get_message()

                if msg:
                    self.__execute_command(msg)
                    self.__ack_message(msg)

        except KeyboardInterrupt:
            print('Bot interrupted. Stopping...')
