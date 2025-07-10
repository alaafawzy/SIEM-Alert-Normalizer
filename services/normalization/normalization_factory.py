from services.normalization.QRadarNormalizer import QRadarNormalizer
from services.normalization.SentinelNormalizer import SentinelNormalizer
from services.normalization.ElasticNormalizer import ElasticNormalizer

class NormalizationFactory:
    @staticmethod
    def get_normalizer(source_type, raw_data):
        normalizers = {
            "qradar": QRadarNormalizer,
            "sentinel": SentinelNormalizer,
            "elastic": ElasticNormalizer
        }
        normalizer_cls = normalizers.get(source_type.lower())
        if normalizer_cls:
            return normalizer_cls(raw_data)
        raise ValueError(f"Unsupported source type: {source_type}")
