<script>
	import AssetsManager from './AssetsManager.svelte';
	import PlaylistService from '$lib/services/playlists';
	import { createEventDispatcher } from 'svelte';
	import PlaylistIslandsSelect from './PlaylistIslandsSelect.svelte';
	import PlaylistScheduleEdit from './PlaylistScheduleEdit.svelte';
	import { is_schedual_active } from '$lib/utils';
	import IconYes from '../icons/IconYes.svelte';
	import IconNo from '../icons/IconNo.svelte';

	export const dispatch = createEventDispatcher();
	export let playlist;
	let submiting = false;
	function submit() {
		submiting = true;
		PlaylistService.updateOrCreatePlaylist(playlist)
			.then((resp) => {
				dispatch('save', playlist);
			})
			.catch((e) => {})
			.finally(() => {
				submiting = false;
			});
	}
</script>

<div class="container mt-5">
	<h2>
		{#if playlist.uuid}
			עריכת פלייליסט: {playlist.name}
		{:else}
			יצירת פלייליסט חדש
		{/if}
	</h2>
	<form action="" method="post" enctype="multipart/form-data">
		<!-- is_active -->
		<!-- <div class="form-group form-check">
			{#if is_schedual_active(playlist.schedule)}
				<IconYes />
			{:else}
				<IconNo />
			{/if}

			<label class="form-check-label" for="is_active">פעיל</label>
		</div> -->
		<!-- is active -->
		<div class="form-group form-check">
			<input
				type="checkbox"
				class="form-check-input"
				id="is_active"
				name="is_active"
				bind:checked={playlist.is_active}
			/>
			<label class="form-check-label" for="is_active">פעיל</label>
		</div>
		<!-- name -->
		<div class="form-group">
			<label for="name">שם</label>
			<input type="text" class="form-control" id="name" name="name" bind:value={playlist.name} />
		</div>
		<!-- islands selection -->
		<div class="form-group">
			<label for="">פעיל במסכים</label>
			<PlaylistIslandsSelect {playlist} />
		</div>

		<!-- schedule -->
		<div class="form-group">
			<label for="schedule"
				>לוח זמנים (
				{#if is_schedual_active(playlist.schedule)}
					<IconYes /> פעיל כרגע
				{:else}
					<IconNo /> לא פעיל כרגע
				{/if})
			</label>
			<PlaylistScheduleEdit bind:playlist />
		</div>
		<button
			type="submit"
			class="btn btn-primary"
			on:click|preventDefault={submit}
			disabled={submiting}>שמור</button
		>
		<AssetsManager bind:playlist />
	</form>
</div>
