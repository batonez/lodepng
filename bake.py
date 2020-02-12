import os
import importlib.util
bakerModuleSpec = importlib.util.spec_from_file_location("baker", os.path.join(os.environ['HATCHERY_SOURCES'], 'baker', 'baker.py'))
baker = importlib.util.module_from_spec(bakerModuleSpec)
bakerModuleSpec.loader.exec_module(baker)

baker.compilerOutputDir = os.path.join(os.environ['HATCHERY_BUILDS'], 'lodepng')

baker.compilerSources = [
os.path.join(os.environ['HATCHERY_VENDOR'], 'lodepng', 'lodepng.cpp'),
]

baker.sanitizeBakeInput()
baker.compile()
