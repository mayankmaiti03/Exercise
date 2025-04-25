SELECT
    d.First_Name || ' ' || d.Last_Name AS Name, -- Concatenates first and last name into one "Name" column
    d.License_Number,                            -- Retrieves the driver's license number
    v.Plate_Number                               -- Retrieves the vehicle's plate number
FROM
    driver d
JOIN
    vehicle v ON d.Vehicle_ID = v.Vehicle_ID     -- Joins driver and vehicle tables using Vehicle_ID
WHERE
    v.Status = 'In Use'                          -- Filters for vehicles that are currently in use
    AND v.Plate_Number LIKE '%0';                -- Filters for plate numbers ending in '0'
