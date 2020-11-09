env_separator = ","
env_keyvalue_separator = "|||"

media_arg_model = "model"
media_arg_date = "date"

# exif
exif_args_per_model = "-Filename<PATH/${model;}/%f%+c%E"
exif_args_per_date = "-Filename<"
exif_file_naming_duplication_rule = "%%-c.%%le"

# env
processing_type_copy = 'COPY'
processing_file_model_prefix = 'MODEL'
keyword_image = 'IMAGE'
keyword_video = 'VIDEO'

ENV_PROCESSING_TYPE_KEY = 'PROCESSING_TYPE'
ENV_PROCESSING_MEDIA_TYPES_KEY = 'PROCESSING_MEDIA_TYPES'
ENV_IMAGE_FILE_TYPES_KEY = 'IMAGE_FILE_TYPES'
ENV_VIDEO_FILE_TYPES_KEY = 'VIDEO_FILE_TYPES'
ENV_PROCESSED_FILE_NAMING_RULE_KEY = 'PROCESSED_FILE_NAMING_RULE'
ENV_PROCESSED_IMAGE_DIR_PATH_KEY = 'PROCESSED_IMAGE_DIR_PATH'
ENV_PROCESSED_VIDEO_DIR_PATH_KEY = 'PROCESSED_VIDEO_DIR_PATH'
ENV_PREFIX_REPLACE_VALUES_KEY = 'PREFIX_REPLACE_VALUES'
ENV_PREFIX_SUFFIX_KEY = 'PREFIX_SUFFIX'

all_env_keys = [
  ENV_PROCESSING_TYPE_KEY, ENV_PROCESSING_MEDIA_TYPES_KEY, ENV_IMAGE_FILE_TYPES_KEY, ENV_VIDEO_FILE_TYPES_KEY,
  ENV_PROCESSED_FILE_NAMING_RULE_KEY, ENV_PROCESSED_IMAGE_DIR_PATH_KEY, ENV_PROCESSED_VIDEO_DIR_PATH_KEY, ENV_PREFIX_REPLACE_VALUES_KEY
]