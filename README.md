# CXBuild

## Download

```bash
cd ~/ && git clone https://github.com/Harry-Cao/cxbuild.git
```

## Setup

### 1. Command line tool

Setup:

```bash
cd ~/cxbuild && make setup
# Then reopen command line to proceed to the next step.
```

Uninstall:

```bash
cd ~/cxbuild && make uninstall
```

### 2. config.json

Create `~/cxbuild/config.json` and setup according to [config.json.example](config.json.example)

### 3. build.py

Download the latest `build.py` and place it to project's root directory: `~/cxbuild/build.py`

## Usage

### 1. List resources

```bash
cxbuild list
```

### 2. Build dependences automatically

- with project index

```bash
cxbuild auto -s 0
```

- or with project name

```bash
cxbuild auto -s project_name
```

### 3. Update and build

```bash
cxbuild u -s 0 && cxbuild b -s 0
```

### 4. More

```bash
cxbuild --help
```
