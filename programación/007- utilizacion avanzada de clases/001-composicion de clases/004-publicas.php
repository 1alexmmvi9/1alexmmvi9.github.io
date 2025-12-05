<?php
	class Persona{
		public $nombre;
		public $apellidos;
		public $edad;
	}
	
	$persona1 = new Persona();
	$persona1->nombre = "Andrés";
	var_dump($persona1);
?>