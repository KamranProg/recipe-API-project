# Forward all commands to app/Makefile automatically

APP_MAKE = make -C app

%:
	@$(APP_MAKE) $@
