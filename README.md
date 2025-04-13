# aap-eda-samples
This repository contains sample rulebooks to provide validation of Event-Driven Ansible (EDA) capabilities in Red Hat Ansible Automation Platform (AAP) 2.5.

## Usage
To make deployment as easy as possible, variable files compatible with [`infra.aap_configuration`](https://github.com/redhat-cop/infra.aap_configuration) are available in the [config-as-code](./config-as-code/) directory. Please ensure you have the required [dependencies](https://github.com/redhat-cop/infra.aap_configuration?tab=readme-ov-file#requirements) installed.

Configure the `aap_hostname`, `aap_username`, and `aap_password` variables either separately or in the [`1_aap_connection_vars.yml`](./config-as-code/1_aap_connection_vars.yml) file. 

> [!IMPORTANT]
> While token authentication is recommended by `infra.aap_configuration`, token authentication is currently not supported by the `ansible.eda` collection. You **must** provide `aap_username` and `aap_password` variables.

## Deployment
Set the `eda_demo_content_state` variable to `present`.

Ex: `ansible-playbook infra.aap_configuration.configure_aap.yml -e aap_configs_dir=./aap-eda-samples/config-as-code/ -e eda_demo_content_state=present`

Upon deployment, the following resources are created:
| Name | Type | Component |
| ---- | ---- | --------- |
| EDA Samples |  Organization | Platform |
| EDA Samples (this repository) |  Project | Automation Decisions |
| Token Event Stream - Demo | Credential | Automation Decisions |
| Debug Token Event Stream - Demo | Event Stream | Automation Decisions |
| AAP Controller - Full Admin for Demo Purposes Only | Credential | Automation Decisions |
| EDA Samples (this repository) | Project | Automation Controller |
| Debug EDA Webhook Message - Demo | Job Template | Automation Controller |

Additionally, the following Rulebook Activations are created in the new "EDA Samples" organization:

| Name | Source | Purpose |
| ---- | ------ | ------- | 
| Debug Incoming Requests from Event Stream - Demo | [`ansible.eda.webhook`](https://github.com/ansible/event-driven-ansible/blob/main/extensions/eda/plugins/event_source/webhook.py) | Examines incoming event payload, validates Event Stream functionality |
| URL Check Good - Demo | [`ansible.eda.url_check`](https://github.com/ansible/event-driven-ansible/blob/main/extensions/eda/plugins/event_source/url_check.py) | Demonstrates source plugin against a known good target, use of variables in rulebook activations |
| URL Check Bad - Demo | [`ansible.eda.url_check`](https://github.com/ansible/event-driven-ansible/blob/main/extensions/eda/plugins/event_source/url_check.py) | Demonstrates source plugin against a known bad target, use of variables in rulebook activations |
| Launch Job Template from Event Stream - Demo | [`ansible.eda.webhook`](https://github.com/ansible/event-driven-ansible/blob/main/extensions/eda/plugins/event_source/webhook.py) | Demonstrates use of variables, integration with AAP Job Templates | 

## Testing
The Rulebook Activations using the `url_check` sources start monitoring automatically. 

To validate the `webhook` sources, a simple python utility script [`webhook.py`](./files/webhook.py) is available to create synthetic events to test the Event Stream functionality and Job Template integration.

To use the script:
- Update the script by [supplying the URL](./files/webhook.py#L3) from the created `Debug Token Event Stream - Demo` Event Stream resource, and [the token value](./files/webhook.py#L4) from the `Token Event Stream - Demo` Credential resource. 
- Update the [data](./files/webhook.py#L7) field(s) if desired; finally, execute `python3 ./files/webhook.py`. 

## Validation
- Review the Rule Audit section of Automation Decisions to see which rules are being triggered, how, and why. 
- Review the Jobs section of Automation Controller to see job template output and the extra variables being passed along from EDA.

## Removal
Set the `eda_demo_content_state` variable to `absent`. All previously created resources are removed.

Ex: `ansible-playbook infra.aap_configuration.configure_aap.yml -e aap_configs_dir=./aap-eda-samples/config-as-code/ -e eda_demo_content_state=absent`
