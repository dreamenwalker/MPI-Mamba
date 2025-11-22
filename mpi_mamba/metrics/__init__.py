from copy import deepcopy

from basicsr.utils.registry import METRIC_REGISTRY

from .rmse import calculate_rmse,calculate_nrmse

__all__ = ['calculate_rmse','calculate_nrmse']


def calculate_metric(data, opt):
    """Calculate metric from data and options.

    Args:
        opt (dict): Configuration. It must contain:
            type (str): Model type.
    """
    opt = deepcopy(opt)
    metric_type = opt.pop('type')
    metric = METRIC_REGISTRY.get(metric_type)(**data, **opt)
    return metric
