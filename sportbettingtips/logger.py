# Librerias Standard
# Standard Libraries
import logging


# ========================================================================== #
def config_logger(
    name='',
    level=logging.INFO,
    format='%(message)s',
    handler=logging.StreamHandler
):
    """ configures a logger """
    _handler = handler()
    _handler.setFormatter(logging.Formatter(_format))
    _logger = logging.getLogger(name)
    _logger.addHandler(_handler)
    _logger.setLevel(level)
    return _logger

logger = config_logger(
    # pylint: disable=invalid-name
    name='eliminar socio',
    level=logging.DEBUG,
    _format='%(levelname)s - [%(processName)s(%(process)d)] [%(asctime)s] - %(filename)s:%(lineno)d: %(message)s'
)


# # Global - not a good practice - just to debug
# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(filename)s:%(lineno)d - %(message)s')
# logging.debug('hello world!')
