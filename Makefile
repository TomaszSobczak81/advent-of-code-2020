docker_compose = docker compose
docker_container = console

build: # Rebuild docker stack
	${docker_compose} build --build-arg DOCKER_USER_ID=`id --user` --build-arg DOCKER_GROUP_ID=`id --group`

up: # Start docker stack in detached mode
	${docker_compose} up --detach --remove-orphans

ps: # Print docker stack status
	${docker_compose} ps

down: # Stop docker stack
	${docker_compose} down

ssh: # SSH into container for work
	${docker_compose} exec ${docker_container} /bin/ash

code_format: # Run code formatting
	${docker_compose} exec ${docker_container} black ./src

run_day_00: # Run a solver for Day 0 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day00

run_day_01: # Run a solver for Day 1 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day01

run_day_02: # Run a solver for Day 2 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day02

run_day_03: # Run a solver for Day 3 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day03

run_day_04: # Run a solver for Day 4 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day04

run_day_05: # Run a solver for Day 5 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day05

run_day_06: # Run a solver for Day 6 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day06

run_day_07: # Run a solver for Day 7 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day07

run_day_08: # Run a solver for Day 8 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day08

run_day_09: # Run a solver for Day 9 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day09

run_day_10: # Run a solver for Day 10 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day10

run_day_11: # Run a solver for Day 11 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day11

run_day_12: # Run a solver for Day 12 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day12

run_day_13: # Run a solver for Day 13 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day13

run_day_14: # Run a solver for Day 14 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day14

run_day_15: # Run a solver for Day 15 solutions
	${docker_compose} exec ${docker_container} python ./src/aoc.py day15
