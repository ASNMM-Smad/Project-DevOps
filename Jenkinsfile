pipeline {
    agent any
    stages{
        stage('Checking GitHub for changes') {
            steps {
              checkout([$class: 'GitSCM', 
                branches: [[name: '*/master']],
                doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: 'CleanCheckout']],
                submoduleCfg: [], 
                userRemoteConfigs: [[url: 'https://github.com/ASNMM-Smad/Project-DevOps']]])
            }
        }
        stage('Building docker images with Docker-Compose'){
            steps{
                py 'python --version'
                py 'docker compose -f ./score_service/docker-compose.yml up'
            }
        }
    }
}