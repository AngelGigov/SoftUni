CREATE VIEW
	view_continents_countries_currencies_details
AS
SELECT
	CONCAT_WS(': ', c.continent_name , c.continent_code) AS continent_details,
	CONCAT_WS(' - ', cn.country_name, cn.capital, cn.area_in_sq_km, 'km2') AS country_information,
	CONCAT(cur.description, ' (', cur.currency_code, ')') as currencies
FROM
	continents as c,
	countries as cn,
	currencies as cur
WHERE
	cn.currency_code = cur.currency_code
	AND
	cn.continent_code = c.continent_code
ORDER BY
	country_information, currencies
;