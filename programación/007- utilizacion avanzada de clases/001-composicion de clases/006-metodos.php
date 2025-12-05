<?php
	class Persona{
		private $nombre;
		private $apellidos;
		private $edad;
		
		public function setNombre($nuevonombre){
			$this->nombre = $nuevonombre;
		}
	}
	
	$persona1 = new Persona();
	$persona1->setNombre("Andrés");
	var_dump($persona1);
?>