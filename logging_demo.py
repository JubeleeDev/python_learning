import logging

logger = logging.getLogger(__name__)

def apply_discount(price: float, percent: float) -> float:
    if price <= 0:
        msg = "price must be positive"
        logger.error(msg)
        raise ValueError(msg)
    elif percent <= 0:
        msg = "percent must be positive"
        logger.error(msg)
        raise ValueError(msg)

    result = price * (1 - percent / 100)
    logger.info("price is %s, percent is %s. Price with discount is %s", price, percent, result)
    return result
    

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level="DEBUG")
    print(apply_discount(100, 5))

    try:
        apply_discount(5,0)
    except ValueError as e:
        pass
