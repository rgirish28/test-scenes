#!/usr/bin/env bash

for curr in {8..20}; do
	for i in {1..5}; do     
		cp scene_pbrt_melanin_${curr}.appleseed scene_pbrt_melanin_${curr}_melratio_${i}.appleseed
	done
done

