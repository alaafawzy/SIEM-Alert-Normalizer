from services.normalization.ElasticNormalizer import ElasticNormalizer
from services.normalization.QRadarNormalizer import QRadarNormalizer
from services.normalization.SentinelNormalizer import SentinelNormalizer

NORMALIZER_MAP = {
    "qradar": QRadarNormalizer,
    "sentinel": SentinelNormalizer,
    "elastic": ElasticNormalizer,
}

def get_normalizer(source_type, raw_data):
    normalizer_class = NORMALIZER_MAP.get(source_type)
    if not normalizer_class:
        raise ValueError(f"No normalizer found for source type: {source_type}")
    return normalizer_class(raw_data)