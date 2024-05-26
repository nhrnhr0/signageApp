<script>
	import IslandDisplay from './IslandDisplay.svelte';

	export let data;
</script>

<!-- grid taking all the screen
one big part up and 4 small parts down
big part: width 100% height 80%
small parts: width 25% height 20%
each part will have a svelte component that will show the playlist (data.islands[x])
-->

<div class="grid">
	<div class="big-part part">
		<IslandDisplay island={data.islands[0]} />
	</div>
	<div class="small-wrapper">
		<div class="small-part part">
			<IslandDisplay island={data.islands[1]} />
		</div>
		<div class="small-part part">
			<IslandDisplay island={data.islands[2]} />
		</div>
		<div class="small-part part">
			<IslandDisplay island={data.islands[3]} />
		</div>
		<div class="small-part part">
			<IslandDisplay island={data.islands[4]} />
		</div>
	</div>
</div>

<style>
	.grid {
		display: grid;
		grid-template-columns: 100%;
		grid-template-rows: 80% 20%;
		height: 100vh;
		overflow: hidden;
	}

	.big-part {
		background-color: #000;
	}

	.small-wrapper {
		display: grid;
		grid-template-columns: 25% 25% 25% 25%;
		grid-template-rows: 100%;
		height: 100%;
	}

	.small-part {
		background-color: #000;
	}

	.part {
		outline: 1px solid black;
	}
</style>
