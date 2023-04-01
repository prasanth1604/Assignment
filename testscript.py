#Question1 - Check the status_code

import requests
import pytest
import json


def test_method1():
    response = requests.get("https://reqres.in/api/users?page=2")
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200


def test_method2():
    response2 = requests.get("https://reqres.in/api/users/23")
    print(response2.text)
    print(response2.status_code)
    assert response2.status_code == 404


def test_method3():
    response3 = requests.get("https://reqres.in/api/users")
    print(response3.status_code)
    print(response3.text)
    assert response3.status_code == 202
    #This is the negative scenario where status_code is incorrectly asserted


#Question No.2
#Test script to check whether the json we got from api is in range or not
#case1 where response time is 0.145 seconds and it is within the range (range = 0.0 to 1.0)
def test_method4():
    min_response_time = 0.0
    max_response_time = 1.0
    response4 = requests.get("https://reqres.in/api/users?page=2")
    time_elapsed = response4.elapsed.total_seconds()
    print(time_elapsed)
    assert min_response_time <= time_elapsed <= max_response_time


#case2 where response time is 0.110 seconds. But time is more than the range we took ie (range = 0.0 to 0.1)
def test_method5():
    min_response5 = 0.0
    max_response5 = 1.0
    response5 = requests.get("https://reqres.in/api/users/23")
    time_elapsed_1 = response5.elapsed.total_seconds()
    print(time_elapsed_1)
    assert min_response5 <= time_elapsed_1<= max_response5


#case3 where response time is 0.0668 seconds and time elapsed is within range i.e (range = 0.0 to 1.0)
def test_method6():
    min_response6 = 0.0
    max_response6 = 1.0
    response6 = requests.get("https://reqres.in/api/unknown")
    time_elapsed_2 = response6.elapsed.total_seconds()
    print(time_elapsed_2)
    assert min_response6 <= time_elapsed_2 <= max_response6


#case4 where response time is way more than within the specified range i.e (range = 0.0 to 1.0)
def test_method7():
    min_response7 = 0.0
    max_response7 = 1.0
    response7 = requests.get("https://reqres.in/api/users?delay=3")
    time7 = response7.elapsed.total_seconds()
    print(time7)
    assert min_response7 <= time7 <= max_response7


#Question 3 - to validate that the response data is correct and in the expected format


def test_program():
    response_format = requests.get("https://reqres.in/api/users/2")
    assert response_format.headers['Content-Type'] == 'application/json; charset=utf-8'
    print(response_format.text)


def test_program1():
    response_format_1 = requests.get("https://reqres.in/api/unknown")
    assert response_format_1.headers['Content-Type'] == 'application/json; charset=utf-8'
    print(response_format_1.text)


#Question4 - to validate the functionality of each API endpoint.

def test_method_add():
    new_data = {
            "name": "morpheus",
            "job": "leader"
           }
    response_add_book = requests.post("https://reqres.in/api/users", data=new_data)
    print(response_add_book.text)
    print(response_add_book.status_code)
    added_id = response_add_book.json()['id']
    print(added_id)
    assert response_add_book.json()['id'] != None
    assert response_add_book.status_code == 201
    #Some data is added to the mentioned api, now we have to delete the book with the help of id number that is generated


def test_method_delete():
    response_delete_book = requests.delete("https://reqres.in/api/users/2"+"{added_id}")
    print(response_delete_book.status_code)
    print(response_delete_book.text)
    assert response_delete_book.status_code == 204



