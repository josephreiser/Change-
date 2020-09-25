cmake_minimum_required(VERSION 3.16)
project(change_coding_challenge_josephreiser)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(change_coding_challenge_josephreiser
        test.py
        README.md)
