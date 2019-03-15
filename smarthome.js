 webiopi().ready(function() {
        		webiopi().setFunction(4,"out");
        		webiopi().setFunction(18,"out");
        		webiopi().setFunction(22,"out");
        		webiopi().setFunction(23,"out");
    
        		
        		var content, button;
        		content = $("#content");
        		
        		button = webiopi().createGPIOButton(4,"FAN 1");
        		content.append(button);
        		
        		button = webiopi().createGPIOButton(18,"FAN 2");
        		content.append(button);
        		
        		button = webiopi().createGPIOButton(22,"LED 1");
        		content.append(button);
        		
        		button = webiopi().createGPIOButton(23,"LED 2");
        		content.append(button);
        		
        	
        		
        });