node() {
  docker {
  
    checkout scm
    stage(‘Build’) {
	sh 'docker-compose -f docker-compose.yml build'
	sh 'docker-compose -f docker-compose.yml up'
}
    
    }
  }
}
