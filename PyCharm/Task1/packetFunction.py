#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def replace_duplicates(replace_char):
    def inner_func(string):
        result = string[0]
        for i in range(1, len(string)):
            if string[i] != string[i-1]:
                result += string[i]
            else:
                result += replace_char
        return result

    return inner_func



