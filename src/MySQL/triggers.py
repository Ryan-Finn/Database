TRIGGERS = dict()

TRIGGERS["status_bu"] = (
    "CREATE TRIGGER status_bu\n"
    "BEFORE UPDATE ON shipments FOR EACH ROW\n"
    "BEGIN\n"
    "    IF NEW.shipment_no != 1 AND NEW.status = 'IN-TRANSIT' AND OLD.status = 'PROCESSING' THEN\n"
    "        SET NEW.shipment_date = CURRENT_TIMESTAMP;\n"
    "    ELSEIF NEW.shipment_no != 1 AND NEW.status = 'DELIVERED' AND OLD.status = 'IN-TRANSIT' THEN\n"
    "        SET NEW.delivery_date = CURRENT_TIMESTAMP;\n"
    "    ELSE\n"
    "        SET NEW.status = OLD.status;\n"
    "        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Shipment status not updated.';\n"
    "    END IF;\n"
    "END"
)
