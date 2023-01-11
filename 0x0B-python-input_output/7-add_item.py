#!/usr/bin/python3

"""A module that adds, loads and save objects using json"""

from sys import argv

old_list = []

new_list = []

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
if len(load_from_json_file('add_item.json')):

    old_list = load_from_json_file('add_item.json')

new_list = [*old_list, *argv[1:]]

save_to_json_file(new_list, 'add_item.json')

print(load_from_json_file('add_item.json'))
