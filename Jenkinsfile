pipeline{
    agent any
    environment {
    PATH = "/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${env.PATH}"
  }
    stages{
        stage("SCM Checkout"){
            steps{
                git branch: 'main', credentialsId: 'ed4599ca-c0c2-4da2-b1f6-ac85d73a02fa', url: 'https://github.com/Saisrivathsan15/myapp.git'
            }
        }
        stage("Ansible playbook"){
            steps{
                sh 'echo $PATH'
               
                ansiblePlaybook installation: 'ansible', inventory: 'hosts', playbook: 'main.yml'
            }
        }
        stage("Zoom chat connection webhook"){
            steps{
                
                zoomSend authToken: 'VkVSU046MDAwtkhDUqL1SBGEOq0jXWkwpVgrBOmvokxkrJpVqxTf2cFrmfpnn6eOfafQ2WGPHyFP4DI', jenkinsProxyUsed: true, message: 'Message from Jenkins', webhookUrl: 'https://applications.zoom.us/addon/v2/jenkins/webhooks/In851XNtRVSBqa46iGzxmw'
            }
        
            
        }
    }
}    