from swebench_docker.utils import get_test_directives
NOOP_PATCH = (
    "diff --git a/empty.file.{nonce}.ignore b/empty.file.{nonce}.ignore\n"
    "new file mode 100644\n"
    "index 0000000..e69de29\n"
)
    log_lines = [line for line in log_lines if line.startswith(">>>>")]