cmake_minimum_required(VERSION 3.15)
project(pesconvert C)

add_library(pesconvert pes.c pes.h)
target_include_directories(pesconvert PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(pesconvert PROPERTIES PUBLIC_HEADER pes.h)
target_compile_definitions(pesconvert PRIVATE PESCONVERT_EXPORT_LIB)
install(TARGETS pesconvert DESTINATION "."
        PUBLIC_HEADER DESTINATION include
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
