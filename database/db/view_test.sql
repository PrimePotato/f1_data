SELECT driver.forename, driver.surname, race.name, race.year, circuit.name, result.time, qualifying.q3
FROM result
JOIN race ON
result.raceId = race.raceId
JOIN circuit ON
circuit.circuitId = race.circuitId
JOIN driver ON
driver.driverId = result.driverId
LEFT JOIN qualifying ON
qualifying.raceId = result.raceId AND qualifying.driverId = driver.driverId
WHERE result.position=1 AND race.circuitId=9
ORDER BY race.year DESC

