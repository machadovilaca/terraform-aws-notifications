PREFIX?=$(shell pwd)

## Tools
BINDIR := $(PREFIX)/bin
export GOBIN :=$(BINDIR)
export PATH := $(GOBIN):$(PATH)

all: init fmt validate tflint tfsec

.PHONY: init
init: ## Initialize a Terraform working directory
	@echo "+ $@"
	@terraform init

.PHONY: fmt
fmt: ## Rewrites terraform files to canonical format
	@echo "+ $@"
	@terraform fmt -check=true -recursive

.PHONY: validate
validate: ## Validates the Terraform files
	@echo "+ $@"
	@AWS_REGION=eu-west-1 terraform validate

.PHONY: tflint
tflint: ## Runs tflint on all Terraform files
	@echo "+ $@"
	@tflint || exit 2

.PHONY: tfsec
tfsec: ## Runs tfsec on all Terraform files
	@echo "+ $@"
	@tfsec $$d || exit 1
