# Changelog

All notable changes to this project will be documented in this file.

## 0.1.3

### Added

- Camera entity is loaded again and plays the printer's HTTP-FLV stream.
- Camera stream switch is loaded.
- Camera card in the example dashboard.

### Fixed

- Camera staying idle with no picture after a printer or Home Assistant restart: `startCapture` is now sent whenever the stream is opened and after the LAN connection reconnects.
- Kobra X `206 Partial Content` stream response is relayed as `200` so ffmpeg/go2rtc accept it.
- MQTT connection now sends keepalive pings and reconnects when the printer stops answering (e.g. after a printer reboot).

## 0.1.2

### Fixed

- Tweaked for missing modelId for Kobra S1 Combo (Thanks fo grigorye)

## 0.1.1

### Added

- Print task sensors:
  - Print task
  - Print status
  - Print progress
  - Current layer
  - Total layers
  - Remaining print time
  - Print time
  - Filament used
  - Task ID

### Changed

- Removed the unstable camera entity from the loaded platforms.
- Camera stream URL is now exposed as an attribute on the Camera available binary sensor instead.

### Fixed

- Avoid Home Assistant camera proxy authentication errors caused by the unsupported FLV-style camera stream.

### Notes

- This version is still in progress.
- No release tag has been created yet.

## 0.1.0 - Initial HACS release

### Added

- Local setup by printer IP address.
- Printer state sensors.
- Nozzle and bed temperature sensors.
- Target nozzle and bed temperature controls.
- Fan speed sensors and controls.
- Firmware version sensor.
- Printer model and IP sensors.
- Feature information sensor.
- Multi-color box status sensor.
- Dynamic filament slot sensors.
- Camera entity.
- Camera light control.
- Refresh data button.
- Reconnect LAN connection button.
- Diagnostics support.
- HACS validation workflow.
- Hassfest validation workflow.
- Integration brand icon.

### Not included

- Firmware update checks.
- Print upload/start.
- Axis movement.
- Filament loading/unloading.
- Filament color changes.
- Cloud account features.
