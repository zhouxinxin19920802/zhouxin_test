# Anylogic 一些常用注意点
---------------------
1.自定义试验的，设置随机发生器代码
```java
    engine.setDefaultRandomGenerator(new Random());
```
上述代码可以设置随机种子，使自带随机的函数生成的值具有随机性，每次都不一样

针对java自带的Math.random(),设置随机发生器的代码为:
```java
    long seed = 12345L; // 设置种子为12345
    Random rand = new Random(seed); // 创建一个使用指定种子的随机数生成器
    System.out.println(rand.nextDouble());
```



2.Anylogic可生成不同平台(Linux，Macos，)



3.Anylogic中读写txt的根目录是项目目录

```java
//int[] swarm_size = new int[] {60};
int[] swarm_size = new int[] {20,30,50,60};
double[] fail_proportion = new double[] {0.2,0.3,0.4,0.5,0.6,0.7};
//double[] fail_proportion = new double[] {0.5};

/*
swarm_size = new int[] {50};
fail_proportion = new double[] {0.1};
*/


// 先把resilience.txt和resilience_average.txt更新下
// resilience.txt的删除和创建
try {
	File resilence_file = new File("resilence.txt");
	if (resilence_file.delete()) {
		System.out.println(
				resilence_file.getName() + " 文件已被删除！");
	} else {
		System.out.println("文件删除失败！");
	}
} catch (Exception e) {
	e.printStackTrace();
}
// 创建文件 resilence.txt
try {
	File resilence_file = new File("resilence.txt");
	if (!resilence_file.exists()) {
		resilence_file.createNewFile();
		System.out.println(
				resilence_file.getName() + " 文件已被创建！");
	}
} catch (Exception e) {
	e.printStackTrace();
}
// resilience_average.txt的删除和创建
try {
	File resilence_file = new File("resilence_average.txt");
	if (resilence_file.delete()) {
		System.out.println(
				resilence_file.getName() + " 文件已被删除！");
	} else {
		System.out.println("文件删除失败！");
	}
} catch (Exception e) {
	e.printStackTrace();
}
// 创建文件 resilence_average.txt
try {
	File resilence_file = new File("resilence_average.txt");
	if (!resilence_file.exists()) {
		resilence_file.createNewFile();
		System.out.println(
				resilence_file.getName() + " 文件已被创建！");
	}
} catch (Exception e) {
	e.printStackTrace();
}




for(int i=0 ; i< swarm_size.length; i++){
	for(int j =0; j<fail_proportion.length;j++ ){
		for(int k=0;k<30;k++){
				// 创建引擎，初始化随机数发生器：
				Engine engine = createEngine();
				engine.setTimeUnit( SECOND );
				// 随机种子（可重现的仿真运行）
				//engine.setDefaultRandomGenerator( new Random( 1 ) );
				engine.setDefaultRandomGenerator(new Random());
				// 同时发生事件的选择模式:
				engine.setSimultaneousEventsSelectionMode( Engine.EVENT_SELECTION_LIFO );
				engine.setStartTime( 0.0 );
				engine.setStartDate( toDate( 2022, MARCH, 10, 0, 0, 0 ) );
				// 设置停止时间：
				engine.setStopTime( 1000.0 );
				// 创建新的根对象：
				Main root = new Main( engine, null, null );
				// TODO在这里设置根对象的参数
				root.setParametersToDefaultValues();
				// root.teamSize = 123;
				// ...
				// 为仿真准备引擎：
				// 仿真过程的参数设置
				
				// 设置是否开起故障检测
				root.open_on = true;
				root.fault_proportion = fail_proportion[j];
				root.file_prefix = swarm_size[i]+"_"+fail_proportion[j]+"_";
				
				engine.start( root );
				// 以快速模式启动仿真：
				engine.runFast();
				// TODO在这里处理仿真结果
				// traceln( "uavs:" );
				// traceln( inspectOf( root.uavs ) );
				// ...
				System.out.println("k:"+ k);
				// 销毁模型：
				engine.stop();
				
		}
	    // 30次计算后，需要先根据resilience.txt计算平均值，存储结果，然后删除resilience.txt，再创建resilience.txt
			
		//System.out.println("i:"+i+" "+"swarm_size:"+swarm_size[i]+" "+"fail_proportion:"+fail_proportion[j]);

		try {
			String executer = "python";
			String file_path = "resilience_average_cal.py";
		
			String[] command_line = new String[]{executer,
					file_path};
			int flag = Runtime.getRuntime().exec(command_line)
					.waitFor();
			System.out.println("End_flag:" + flag);
			System.out.println("End");
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
	
		// resilience.txt的删除和创建
		try {
			File resilence_file = new File("resilence.txt");
			if (resilence_file.delete()) {
				System.out.println(
						resilence_file.getName() + " 文件已被删除！");
			} else {
				System.out.println("文件删除失败！");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		// 创建文件 resilence.txt
		try {
			File resilence_file = new File("resilence.txt");
			if (!resilence_file.exists()) {
				resilence_file.createNewFile();
				System.out.println(
						resilence_file.getName() + " 文件已被创建！");
			}
		} catch (Exception e) {
			e.printStackTrace();
	    } 
	}
}
/*
try {
		//System.out.println("执行python脚本");
	    String executer= "python";
	    String file_path = "resilience_same_failure_rate1.py";
	    
	    String[] command_line = new String[] {executer, file_path};
		int flag = Runtime.getRuntime().exec(command_line).waitFor();
		//System.out.println("flag:"+flag);
    } catch(Exception ex){
    	 ex.printStackTrace(); 
}
*/
```



4.Anylogic自带log可以支持各种格式输出，只是不带行号输出，但可以用

