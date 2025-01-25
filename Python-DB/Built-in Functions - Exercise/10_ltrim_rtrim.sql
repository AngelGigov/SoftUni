SELECT
	LTRIM(peak_name, 'M') as left_trim,
	RTRIM(peak_name, 'm') as left_trim
FROM
	peaks;