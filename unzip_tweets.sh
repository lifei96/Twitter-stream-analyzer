#!/bin/bash
for year in ./tweets/*
do
    for month in $year/*
    do
        for day in $month/*
        do
            for hour in $day/*
            do
                bzip2 -d $hour/*
            done
        done
    done
done

