PROJECT_DIR := $(shell pwd)
ZSHRC := $(HOME)/.zshrc
ALIAS_FUNC := 'cxbuild() { \
    if command -v python3 >/dev/null 2>&1; then \
        python3 $(PROJECT_DIR)/run.py "$$@"; \
    elif command -v python >/dev/null 2>&1; then \
        python $(PROJECT_DIR)/run.py "$$@"; \
    else \
        echo "Error: Python is not installed."; \
        return 1; \
    fi; \
}'

.PHONY: setup uninstall

setup:
	@if ! grep -q "cxbuild()" $(ZSHRC) 2>/dev/null; then \
		echo "" >> $(ZSHRC); \
		echo "# CXBuild function" >> $(ZSHRC); \
		echo $$ALIAS_FUNC >> $(ZSHRC); \
	else \
		echo "cxbuild function already exists"; \
	fi

uninstall:
	@if [ -f $(ZSHRC) ]; then \
		sed -i.bak '/# CXBuild function/d; /cxbuild()/,/^}/d' $(ZSHRC); \
	else \
		echo "~/.zshrc file not found"; \
	fi