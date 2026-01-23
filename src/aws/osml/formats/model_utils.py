#  Copyright 2026-2026 General Atomics Integrated Intelligence, Inc.

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

serializer_config = SerializerConfig(pretty_print=False)

sicd_context = XmlContext(models_package=("aws.osml.formats.sicd.models"))
sicd_parser = XmlParser(context=sicd_context)
sicd_serializer = XmlSerializer(context=sicd_context, config=serializer_config)
sidd_context = XmlContext(models_package=("aws.osml.formats.sidd.models"))
sidd_parser = XmlParser(context=sidd_context)
sidd_serializer = XmlSerializer(context=sidd_context, config=serializer_config)
