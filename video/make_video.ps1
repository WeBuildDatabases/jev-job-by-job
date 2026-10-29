# Builds jev-video.mp4 (voice) and jev-video-silent.mp4 (captions only).
# Steps: record the voice phrase by phrase (voice.py), draw one SVG per frame (video.py), render with Edge, encode.
# Needs: Python with Pillow; piper-tts and a Piper voice (set PIPER_VOICE, and PIPER_DEPS if installed with --target);
#        Node with Playwright; Microsoft Edge; imageio-ffmpeg (pip install imageio-ffmpeg).
param([string]$Playwright = "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules\playwright")
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$build = Join-Path $here 'build'
python (Join-Path $here 'voice.py')
python (Join-Path $here 'video.py') frames (Join-Path $build 'svg')
$env:PLAYWRIGHT_MODULE = $Playwright
node (Join-Path $here 'render_frames.mjs') (Join-Path $build 'svg') (Join-Path $build 'png')
$ffmpeg = python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
& $ffmpeg -y -loglevel error -framerate 30 -i (Join-Path $build 'png\f%04d.png') -i (Join-Path $build 'vo_mix.wav') `
  -c:v libx264 -pix_fmt yuv420p -crf 18 -preset slow -movflags +faststart -c:a aac -b:a 160k -shortest (Join-Path $here 'jev-video.mp4')
& $ffmpeg -y -loglevel error -framerate 30 -i (Join-Path $build 'png\f%04d.png') `
  -c:v libx264 -pix_fmt yuv420p -crf 18 -preset slow -movflags +faststart (Join-Path $here 'jev-video-silent.mp4')
Remove-Item -Recurse -Force (Join-Path $build 'svg'), (Join-Path $build 'png')
Write-Output 'built jev-video.mp4 and jev-video-silent.mp4'
