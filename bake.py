import os
import baker

baker.compilerOutputDir = os.path.join(os.environ['HATCHERY_BUILDS'], 'lodepng')

baker.compilerSources = [
os.path.join(os.environ['HATCHERY_SOURCES'], 'lodepng', 'lodepng.cpp'),
]

baker.sanitizeBakeInput()
baker.compile()