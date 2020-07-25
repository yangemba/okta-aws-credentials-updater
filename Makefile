start_updater:
	docker build -t okta_aws_updater_image .;
	docker-compose up -d;
