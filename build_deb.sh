#!/usr/bin/env bash
set -euo pipefail

APP_NAME="countdown-deb"
VERSION="${1:-1.0.0}"
ARCH="all"
BUILD_DIR="dist/${APP_NAME}_${VERSION}_${ARCH}"

echo "Preparando estructura del paquete en: ${BUILD_DIR}"
rm -rf "${BUILD_DIR}"

mkdir -p "${BUILD_DIR}/DEBIAN"
mkdir -p "${BUILD_DIR}/usr/bin"
mkdir -p "${BUILD_DIR}/usr/share/applications"

cat > "${BUILD_DIR}/DEBIAN/control" <<EOF
Package: ${APP_NAME}
Version: ${VERSION}
Section: utils
Priority: optional
Architecture: ${ARCH}
Depends: python3, python3-tk
Maintainer: Cursor Cloud Agent <agent@example.com>
Description: Aplicacion de escritorio de cuenta regresiva
 Temporizador grafico simple con inicio, pausa y reinicio.
EOF

install -m 755 "countdown_timer.py" "${BUILD_DIR}/usr/bin/${APP_NAME}"

cat > "${BUILD_DIR}/usr/share/applications/${APP_NAME}.desktop" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Contador hacia atras
Comment=Temporizador de cuenta regresiva
Exec=${APP_NAME}
Terminal=false
Categories=Utility;
EOF

OUTPUT_DEB="dist/${APP_NAME}_${VERSION}_${ARCH}.deb"
dpkg-deb --build "${BUILD_DIR}" "${OUTPUT_DEB}"
echo "Paquete generado: ${OUTPUT_DEB}"
