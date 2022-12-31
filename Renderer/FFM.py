import errno
import shlex
import subprocess
class FFmpeg(object):
    def __init__(
        self, executable="ffmpeg.exe", global_options=None, inputs=None, outputs=None):
        self.executable = executable
        self._cmd = [executable]
        global_options = global_options or []
        if _is_sequence(global_options):
            normalized_global_options = []
            for opt in global_options:
                normalized_global_options += shlex.split(opt)
        else:
            normalized_global_options = shlex.split(global_options)

        self._cmd += normalized_global_options
        self._cmd += _merge_args_opts(inputs, add_input_option=True)
        self._cmd += _merge_args_opts(outputs)

        self.cmd = subprocess.list2cmdline(self._cmd)
        self.process = None

    def __repr__(self):
        return "<{0!r} {1!r}>".format(self.__class__.__name__, self.cmd)

    def run(self, input_data=None, stdout=None, stderr=None, env=None):
        try:
            self.process = subprocess.Popen(
                self._cmd, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr, env=env
            )
        except OSError as e:
            if e.errno == errno.ENOENT:
                raise FFExecutableNotFoundError(
                    "Executable '{0}' not found".format(self.executable)
                )
            else:
                raise

        out = self.process.communicate(input=input_data)
        if self.process.returncode != 0:
            raise FFRuntimeError(self.cmd, self.process.returncode, out[0], out[1])

        return out


class FFprobe(FFmpeg):


    def __init__(self, executable="ffprobe", global_options="", inputs=None):
      
        super(FFprobe, self).__init__(
            executable=executable, global_options=global_options, inputs=inputs)


class FFExecutableNotFoundError(Exception):
    """Raise when FFmpeg/FFprobe executable was not found."""


class FFRuntimeError(Exception):


    def __init__(self, cmd, exit_code, stdout, stderr):
        self.cmd = cmd
        self.exit_code = exit_code
        self.stdout = stdout
        self.stderr = stderr

        message = "`{0}` exited with status {1}\n\nSTDOUT:\n{2}\n\nSTDERR:\n{3}".format(
            self.cmd, exit_code, (stdout or b"").decode(), (stderr or b"").decode()
        )

        super(FFRuntimeError, self).__init__(message)


def _is_sequence(obj):

    return hasattr(obj, "__iter__") and not isinstance(obj, str)


def _merge_args_opts(args_opts_dict, **kwargs):

    merged = []

    if not args_opts_dict:
        return merged

    for arg, opt in args_opts_dict.items():
        if not _is_sequence(opt):
            opt = shlex.split(opt or "")
        merged += opt

        if not arg:
            continue

        if "add_input_option" in kwargs:
            merged.append("-i")

        merged.append(arg)

    return merged