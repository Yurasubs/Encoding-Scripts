# Imports
import vapoursynth as vs
# getting Vapoursynth core
core = vs.core
# Loading Plugins
core.std.LoadPlugin(path="C:/Program Files/Hybrid/64bit/vsfilters/DebandFilter/Flash3kDeband/flash3kyuu_deband.dll")
core.std.LoadPlugin(path="C:/Program Files/Hybrid/64bit/vsfilters/SourceFilter/LSmashSource/vslsmashsource.dll")
# source: ''
# current color space: YUV420P8, bit depth: 8, resolution: 1920x1080, fps: 23.976, color matrix: 709, yuv luminance scale: limited, scanorder: progressive
# Loading Video using LWLibavSource
clip = core.lsmas.LWLibavSource(source="", format="YUV420P8", cache=0, prefer_hw=0)
# Setting color matrix to 709.
clip = core.std.SetFrameProps(clip, _Matrix=1)
clip = clip if not core.text.FrameProps(clip,'_Transfer') else core.std.SetFrameProps(clip, _Transfer=1)
clip = clip if not core.text.FrameProps(clip,'_Primaries') else core.std.SetFrameProps(clip, _Primaries=1)
# Setting color range to TV (limited) range.
clip = core.std.SetFrameProp(clip=clip, prop="_ColorRange", intval=1)
# making sure frame rate is set to 23.976
clip = core.std.AssumeFPS(clip=clip, fpsnum=24000, fpsden=1001)
# debanding using f3kdb
clip = core.f3kdb.Deband(clip, random_algo_ref=2, random_algo_grain=2, keep_tv_range=True, output_depth=8)
# adjusting output color from: YUV420P8 to YUV420P10 for x264Model
clip = core.resize.Bicubic(clip=clip, format=vs.YUV420P10, range_s="limited")
# set output frame rate to 23.976fps
clip = core.std.AssumeFPS(clip=clip, fpsnum=24000, fpsden=1001)
# Output
clip.set_output()
