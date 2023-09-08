import common

def copy(a):
	new_a = [[None for i in range(6)] for j in range(6)]
	for y in range(6):
		for x in range(6):
			new_a[y][x] = a[y][x]
	return new_a


def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	# 
	convergence = False

	while(not convergence):
		old_values = copy(values)
		
		#for every block
		for y in range(6):
			for x in range(6):
				#if it's the hungry customer
				if map[y][x] == 2:
					values[y][x] = delivery_fee
					policies[y][x] = common.constants.EXIT
				#if it's the rival pizza joint
				elif map[y][x] == 3:
					values[y][x] = -dronerepair_cost
					policies[y][x] = common.constants.EXIT
				#calculate V(k+1)
				else:
					best_q = float('-inf')
					best_a = 0
					#calculate the q_states
					for action in range(1, 9):
						#south/off
						if action == 1:
							q = 0
							if y + 1 <= 5:
								q += 0.7 * (-battery_drop_cost + discount * values[y + 1][x])
							else:
								q += 0.7 * (-battery_drop_cost + discount * values[y][x])
							if x + 1 <= 5:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x + 1])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])
							if x - 1 >= 0:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x - 1])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])

							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.SOFF

						#west/off
						if action == 2:
							q = 0
							if x - 1 >= 0:
								q += 0.7 * (-battery_drop_cost + discount * values[y][x - 1])
							else:
								q += 0.7 * (-battery_drop_cost + discount * values[y][x])
							if y + 1 <= 5:
								q += 0.15 * (-battery_drop_cost + discount * values[y + 1][x])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])
							if y - 1 >= 0:
								q += 0.15 * (-battery_drop_cost + discount * values[y - 1][x])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])

							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.WOFF


						#north/off
						if action == 3:
							q = 0
							if y - 1 >= 0:
								q += 0.7 * (-battery_drop_cost + discount * values[y - 1][x])
							else:
								q += 0.7 * (-battery_drop_cost + discount * values[y][x])
							if x + 1 <= 5:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x + 1])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])
							if x - 1 >= 0:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x - 1])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])

							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.NOFF


						#east/off
						if action == 4:
							q = 0
							if x + 1 <= 5:
								q += 0.7 * (-battery_drop_cost + discount * values[y][x + 1])
							else:
								q += 0.7 * (-battery_drop_cost + discount * values[y][x])
							if y + 1 <= 5:
								q += 0.15 * (-battery_drop_cost + discount * values[y + 1][x])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])
							if y - 1 >= 0:
								q += 0.15 * (-battery_drop_cost + discount * values[y - 1][x])
							else:
								q += 0.15 * (-battery_drop_cost + discount * values[y][x])
							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.EOFF


						#south/on
						if action == 5:
							q = 0
							if y + 1 <= 5:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y + 1][x])
							else:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y][x])
							if x + 1 <= 5:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x + 1])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])
							if x - 1 >= 0:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x - 1])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])

							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.SON

						#west/on
						if action == 6:
							q = 0
							if x - 1 >= 0:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y][x - 1])
							else:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y][x])
							if y + 1 <= 5:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y + 1][x])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])
							if y - 1 >= 0:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y - 1][x])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])

							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.WON


						#north/on
						if action == 7:
							q = 0
							if y - 1 >= 0:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y - 1][x])
							else:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y][x])
							if x + 1 <= 5:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x + 1])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])
							if x - 1 >= 0:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x - 1])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])

							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.NON


						#east/on
						if action == 8:
							q = 0
							if x + 1 <= 5:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y][x + 1])
							else:
								q += 0.8 * (-2*battery_drop_cost + discount * values[y][x])
							if y + 1 <= 5:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y + 1][x])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])
							if y - 1 >= 0:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y - 1][x])
							else:
								q += 0.1 * (-2*battery_drop_cost + discount * values[y][x])

							if q > best_q + 0.0001:
								best_q = q
								best_a = common.constants.EON
					
					#find the max q_state and the acction to get to that q_state
					values[y][x] = best_q
					policies[y][x] = best_a
		
		#Check convergence
		convergence = True
		for y in range(6):
			for x in range(6):
				if old_values[y][x] == 0:
					convergence = False
					break
				else:
					if abs(old_values[y][x] - values[y][x]) > .0000000000000000000000000000000000000001:
						convergence = False
						break
	
	for y in range(6):
		for x in range(6):
			if map[y][x] == 1:
				return values[y][x]
