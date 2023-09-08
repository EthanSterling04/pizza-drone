# Pizza Drone

A path planner to help a pizza chain deliver food to their customers using drones. This planner uses the **Markov decision process** and **reinforcement learning** to train the drone.

## Description

A pizza chain wants to deliver food to its customers using drones. As this is a pilot program they started in a small town of size 6 blocks from west to east by 6 blocks from north to south.

**Things to be aware of:**
- Rival pizza places own some of the blocks and they will shoot down the drones if they fly over them.
- The company pays to charge the drone battery so the shorter the flight, the better.
- Wind can be strong and the drone does not always move in the direction it wants to move.
- All drones come with a special propulsion system that requires extra battery but reduces the impact of the wind in the flight.
- Drones can move only in 4 directions (south, west, north, east).
- Drones can not fall from the map so they bounce against the limits.
- There will be exactly 1 customer, exactly 1 pizza shop, and any number of rivals (including 0)

Due to the wind, every time the drone attempts to move in one direction it has a 70% chance of succeeding and 30% chance of going sideways (15% each side). The special propulsion system improves the results to an 80% chance of success and 20% chance of going sideways (10% each side) but it doubles the battery consumption when it is on.

### Map and Actions

The program will receive a 6x6 map, represented in a 2D array, and must return the recommended actions for the drone in each block.

**The values you will find on the map are:**
* 0 - Empty block
* 1 - The pizza shop
* 2 - The hungry customer 3 - Rival pizza places

<table>
<tr><th>Example map:</th><th>This will be represented by the following array:</th></tr>
<tr><td>

|   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
|   | 1 |   |   | 3 |   |
|  ‎ |   |   |   |   |   |
|  ‎ |   |   |   |   |   |
|   |   | 3 |   |   |   |
|   |   |   |   | 2 |   |

</td><td>

```
map[0]= {0,0,0,0,0,0};
map[1]= {0,1,0,0,3,0}; 
map[2]= {0,0,0,0,0,0}; 
map[3]= {0,0,0,0,0,0}; 
map[4]= {0,0,3,0,0,0};
map[5]= {0,0,0,0,2,0};
```

</td></tr> </table>

**The possible actions are:**
1. South with special propulsion OFF
2. West with special propulsion OFF
3. North with special propulsion OFF
4. East with special propulsion OFF
5. South with special propulsion ON
6. West with special propulsion ON
7. North with special propulsion ON
8. East with special propulsion ON

## Specification

### _drone_flight_planner(map, policies, values delivery_fee, battery_drop_cost, dronerepair_cost, discount)_

This function receives:
- A bi-dimensional structure called ```map``` containing the location of all elements.
- An empty bidimensional structure called ```policies``` that is required to be filled up with the recommended actions for each block.
- An empty bidimensional structure called ```values``` that is required to be filled up with the expected utility of each block under optimal action.
- A float called ```delivery_fee``` with the value of the reward for delivering the food to the hungry customer.
- A float called ```battery_drop_cost``` with the negative reward for each step the drone is flying with special propulsion OFF (i.e. living cost), the negative reward with special propulsion on is ```2*battery_drop_cost```.
- A float called ```dronerepair_cost``` with the cost of replacing the shot-down drone.
- A float called ```discount``` which is the discount of future values (i.e. gamma).

The function returns:
- The expected utility of the job.

The function modifies:
- The ```policies``` structure, by entering the optimal policy for each block.
- The ```values``` structure, by entering the expected utility of each block under optimal policy.

If there is a tie in values due to actions, priority is given to non-special actions, if there is still a tie priority is given in the following way: south>west>north>east.
