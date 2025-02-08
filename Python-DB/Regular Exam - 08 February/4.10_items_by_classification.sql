CREATE OR REPLACE FUNCTION udf_classification_items_count(classification_name VARCHAR(30))
RETURNS TEXT
AS
$$
DECLARE
    item_count INT;
BEGIN
    SELECT COUNT(*) INTO item_count
    FROM items i
    JOIN classifications c ON i.classification_id = c.id
    WHERE c.name = classification_name;

    IF item_count > 0 THEN
        RETURN 'Found ' || item_count || ' items.';
    ELSE
        RETURN 'No items found.';
    END IF;
END;
$$ LANGUAGE plpgsql;