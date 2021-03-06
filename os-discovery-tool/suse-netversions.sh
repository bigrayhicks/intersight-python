#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
hwinfocmd=`which hwinfo`
modinfocmd=`which modinfo`
${hwinfocmd} --network | grep Driver: | awk '{print $2}' | xargs ${modinfocmd} | \
	grep ^version: | awk -F":[[:space:]]+" '{print $2}'
