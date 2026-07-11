# Contador hacia atras (.deb)

Aplicacion de escritorio hecha en Python/Tkinter que realiza una cuenta regresiva con botones de:

- Iniciar
- Pausar
- Reiniciar

## Requisitos

- Debian/Ubuntu (o derivadas)
- `python3`
- `python3-tk`
- `dpkg-deb`

## Generar el paquete `.deb`

```bash
chmod +x build_deb.sh
./build_deb.sh
```

Opcionalmente puedes pasar una version:

```bash
./build_deb.sh 1.0.1
```

El archivo se crea en:

```text
dist/countdown-deb_<version>_all.deb
```

## Instalar

```bash
sudo apt install ./dist/countdown-deb_1.0.0_all.deb
```

## Ejecutar

Desde menu de aplicaciones: **Contador hacia atras**  
o por terminal:

```bash
countdown-deb
```
