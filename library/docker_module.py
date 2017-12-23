#!/usr/bin/python

import  json
from ansible.module_utils.basic import AnsibleModule
import docker

#Main Entry point for the module
def main():

    # Instantiate the Ansible Module which will retrieve the value of our image_name variab
    module = AnsibleModule(argument_spec= dict( image_name = dict(required=True, type='str')))
    # Set the value of image to the value of module.params['image_name']
    image = module.params['image_name']
    # Connect's to the docker 
    client = docker.from_env()
    # Pulling image form docker-hub
    client.images.pull(image)
    
    #message = client.images.list()
    
    print (json.dumps({
        "Message" : "Image uploaded"
    }))

    module.exit_json(changed=True, keyword=value)
    module.exit_json(changed=False, msg='error message', keyword=value)

if __name__ == '__main__':
    main()

