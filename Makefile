PROJECT_DIR := $(shell pwd)
ZSHRC := $(HOME)/.zshrc
ALIAS_LINE := alias cxbuild='python $(PROJECT_DIR)/run.py'

.PHONY: setup uninstall

setup:
	@if ! grep -q "alias cxbuild=" $(ZSHRC) 2>/dev/null; then \
		echo "" >> $(ZSHRC); \
		echo "# CXBuild alias" >> $(ZSHRC); \
		echo "$(ALIAS_LINE)" >> $(ZSHRC); \
	else \
		echo "cxbuild alias already exists"; \
	fi

uninstall:
	@if [ -f $(ZSHRC) ]; then \
		sed -i.bak '/# CXBuild alias/d; /alias cxbuild=/d' $(ZSHRC); \
	else \
		echo "~/.zshrc file not found"; \
	fi